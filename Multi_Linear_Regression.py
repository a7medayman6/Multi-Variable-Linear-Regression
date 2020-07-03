import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

data = pd.read_csv("student-mat.csv", sep = ';')

#the actual attribute to use in the regression
data = data[ ["age", "health", "freetime", "studytime", "absences", "G1", "G2", "G3"] ]

#the name of the prediction attribute 
predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1) 

regr = LinearRegression()
regr.fit(x_train, y_train)

score = regr.score(x_test, y_test)
print("Score\t", score)

predictions = np.rint(regr.predict(x_test))


print("X\t\t\t Y\tPrediction")
i = 0
for pred in predictions:
    print (x_test[i], '\t', y_test[i], '\t', pred)
    i+=1