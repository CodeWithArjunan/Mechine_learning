import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Data Collection
df = pd.read_csv('heart.csv')
print(df)

#Data preprocessing
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['sex'] = le.fit_transform(df['sex'])
df['chestPainType'] = le.fit_transform(df['chestPainType'])
df['RestingECG'] = le.fit_transform(dff['RestingECG'])
df['ExerciseAngina'] = le.fit_transform(df['ExerciseAngina'])
df['ST_slope'] = le.fit_transform(df['ST_slope'])

#Before training Setup
x = df.drop(coloumns='HeartDisease')
y = df['HeartDisease']
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=12)

print("DF",df.shope)
print("x_train",x_train.shope)
print("x_test",x_test.shope)
print("y_train",y_train.shope)
print("y_test",y_test.shope)

#Training Model
from sklearn.naive_layes import GaussianNB
NB=GaussianNB()

NB.fit(x_train,y_train)


#Model Evalution
y_pred = NB.predict(x_test)
print('y_pred',y_pred)
print('y_test',y_test)

from sklearn.metrics import accuracy_score
print("Accuracy is:",accuracy_score(y_test,y_pred))

#Model prediction

testPrediction = NB.predict([[19,1,4,120,166,0,1,138,0,0,2]])
if testPrediction == 1:
    print("The Patient have Heart disease, please consul the doctor")











