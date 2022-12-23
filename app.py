from flask import Flask,render_template,request,url_for,redirect,session
import pickle
import numpy as np
from sqlite3 import *

app=Flask(__name__)
app.secret_key="pg1412"

@app.route("/",methods=["GET","POST"])
def home():
	if "un" in session:
		if request.method=="POST":
			if "submit2" in request.form:
				session.pop('un',None)
				return redirect(url_for('login'))
			if "submit1" in request.form:
				S1 = {"male":1,"female":2}
				SM1 = {"yes":1,"no":2}
				R1 = {"northeast":1,"northwest":2,"southeast":3,"southwest":4}
				frame=[]
				f=None
				model=None
				try:
					f=open("ins.model","rb")
					model=pickle.load(f)
				except Exception as e:
					print("issue ",e)
				finally:
					if f is not None:
						f.close()
				if model is not None:
					msg1="Age is Invalid : Must be a Integer"
					msg2="BMI is Invalid : must be > 0.1"
					try:
						iage=int(request.form["age"])
						if iage <= 0:
							raise ValueError(msg1)
					except ValueError:
						return render_template("home.html",msg=msg1)
					else:
						frame.append(iage)
					isex=request.form["sex"]
					if isex in S1:
						frame.append(S1[isex])
					try:
						ibmi=float(request.form["bmi"])
						if ibmi<=0:
							raise ValueError(msg2)
					except ValueError:
						return render_template("home.html",msg=msg2)
					else:
						frame.append(ibmi)
					ichn=int(request.form["children"])
					frame.append(ichn)
					ismk=request.form["smoker"]
					if ismk in SM1:
						frame.append(SM1[ismk])
					ireg=request.form["region"]
					if ireg in R1:
						frame.append(R1[ireg])
			
					ans=model.predict([frame])
					msg="Medical insurance cost in $ : " + str(np.round(ans[0],2)) 
					return render_template("home.html",msg=msg)
				else:
					print("model issue")
			

		else:
			return render_template("home.html")
		
	else:
		return redirect(url_for('login'))


	


@app.route("/signup",methods=["GET","POST"])
def signup():
	if "un" in session:
		return redirect(url_for("home"))
	if request.method=="POST":
		un = request.form["un"]
		pw1 = request.form["pw1"]
		pw2 = request.form["pw2"]		
		if pw1==pw2:
			con=None
			try:
				con=connect("kc.db")
				cursor=con.cursor()
				sql="insert into users values('%s','%s')"
				cursor.execute(sql %(un,pw1))
				con.commit()
				return redirect(url_for('login'))
			except Exception as e:
				con.rollback()
				return render_template("signup.html",msg="User already exists -> " + str(e))
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html",msg="Password did not match")
	else:
		return render_template("signup.html")

@app.route("/login",methods=["GET","POST"])
def login():
	if "un" in session:
		return redirect(url_for("home"))
	if request.method=="POST":
		un = request.form["un"]
		pw = request.form["pw"]
		con=None
		try:
			con=connect("kc.db")
			cursor=con.cursor()
			sql="select * from users where username='%s' and password='%s'"
			cursor.execute(sql %(un,pw))
			data=cursor.fetchall()
			if len(data) == 0:
				return render_template("login.html",msg="Invalid Login")
			else:
				session["un"]=un
				return redirect(url_for('home'))
		except Exception as e:
			return render_template("login.html",msg=str(e))
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")

@app.errorhandler(404)
def not_found(e):
	return redirect(url_for('login'))



if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)

			