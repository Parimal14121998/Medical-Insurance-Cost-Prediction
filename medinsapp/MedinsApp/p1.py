#MODEL creation file which creates ins.model file

#import lib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

data=pd.read_csv("insurance.csv")
#print(data.head())

#understand data
res=data.isnull().sum()
#print(res)

#cat data

data=data.replace({"sex":{"male":1,"female":2}})
data=data.replace({"smoker":{"yes":1,"no":2}})
data=data.replace({"region":{"northeast":1,"northwest":2,"southeast":3,"southwest":4}})
data.head()

#f&t
f=data.drop(['charges'],axis=1)
t=data['charges']


#train_test_split
x_train,x_test,y_train,y_test=train_test_split(f,t,test_size=0.2,random_state=11)

#model
rf = RandomForestRegressor(n_estimators=10)
rf.fit(f,t)
#print(rf.score(x_train, y_train))
#print(rf.score(x_test,y_test))

#save the model
f=None
try:
	f=open("ins.model","wb")
	pickle.dump(rf,f)
except Exception as e:
	print("issue ",e)
finally:
	if f is not None:
		f.close()


    



