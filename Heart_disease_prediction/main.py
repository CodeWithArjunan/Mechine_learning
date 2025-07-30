import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Data Collection
df = pd.read_csv('hearts.csv')
print(df)

#Data preprocessing
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Sex'] = le.fit_transform(df['Sex'])
df['ChestPainType'] = le.fit_transform(df['ChestPainType'])
df['RestingECG'] = le.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = le.fit_transform(df['ExerciseAngina'])
df['ST_Slope'] = le.fit_transform(df['ST_Slope'])

#Before training Setup
x = df.drop(columns='HeartDisease')
y = df['HeartDisease']
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=12)

print("DF",df.shape)
print("x_train",x_train.shape)
print("x_test",x_test.shape)
print("y_train",y_train.shape)
print("y_test",y_test.shape)

#Training Model
from sklearn.naive_bayes import GaussianNB
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

else:
    print("The patient Normal")










