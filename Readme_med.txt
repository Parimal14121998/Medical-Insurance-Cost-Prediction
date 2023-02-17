Title : Medical Insurance Cost Prediction

Webapp url : http://parimalgupta2medins.pythonanywhere.com/

About :
In the project, we will try to extract some insights from a dataset that contains details about the background of people who is purchasing medical insurance along with what amount of premium is charged to those individuals.
we will apply Machine Learning Regression algorithm using supervised learning to predict Medical Insurance costs.

Motivation:
To provide a web application which easily provides annual premium charges for Health Insurance to the customer through quick prediction .

Tools/Libraries Used:
Python ,Flask ,Jupyter, ML Regression Algorithms , scikitLearn, Matplotlib , seaborn , pandas , Html Forms , Session

Usage:
Customers can directly use the flask based webapp , provide there inputs and determine insurance amount . Besides there is signup/login based authentication approach to have secure  endpoints.

Procedure:
1) The jupyter notebook depicts the whole ML Lifecycle discussed as :
Loading dataset
Data Preprocessing [null and categorical]
Exploratory Data Analysis [Univariate & Multivariate Analysis ]
Feature Engineering
Correlation using HeatMap
Feature Selection
Train Test Split 
Model Selection by comparing different Regression Models
2)Model Deployment using Flask for which code is written in app.py

Implementation Logic:
1)Refer this Readme to know a quick overview.
2)Refer the Jupyter notebook file [.ipynb] to understand about the whole ML Lifecycle.
3)Model Deployment using Flask
i)From p1.py we create ins.model file which is our model creation file 
ii) app.py -> Tells us about the code/logic ,signup/login approach 
iii) templates folder for html ; rendering the display/output.
iv)kc.db stores login/signup data credentials.
 

Observations:
After EDA we knew how charges is correlated with age,BMI,smoker features using graphs.
And after comparing score of Regression models; Random Forest Regressor performs best wrt to train_data{ Accuracy : 96% } and test_data {Accuracy : 86%}. 
For more analysis , visualisation and depiction refer attached jupyter notebook .

Conclusion:
Out of all models RandomForest Regression provides best fit.
The prediction made by this model is close to real values , so we chose it .
We gathered some insights about data through various graphs which depicts as similar to real life scenario
and understood patterns in the relation between the independent features and the premium charged from the buyers.



