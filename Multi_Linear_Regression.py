import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from matplotlib import style 
import pickle
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from methods import *


data = pd.read_csv("student-mat.csv", sep = ';')

#the actual attribute to use in the regression
data = data[ ["age", "health", "freetime", "studytime", "absences", "G1", "G2", "G3"] ]

#the name of the prediction attribute 
predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

#split the data set to test and train data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) 

file_name = "model.pickle"

#comment untile print (best_score) after finding the best score you want, so you don't have to train the model each run  

"""
training_times = 10000
best_score = 0
for _ in range(training_times):
    #split the data set to test and train data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) 

    #creating a LinearRegeression object
    model = LinearRegression()
    #training the model
    model.fit(x_train, y_train)

    #score is how fit the model is
    #getting the score and printing it
    score = model.score(x_test, y_test)


    if best_score < score:
        print ("A better Score!")
        best_score = score
        with open(file_name, "wb") as file:
            pickle.dump(model, file)
            file.close() 
    
    #print("Score\t", score)

print("Best Score\t", best_score, '\n')

"""

#read the best model into the model variable from the file
pickle_reader = open(file_name, 'rb')
model = pickle.load(pickle_reader)


#rounding the prediction to the nearest whole number.
predictions = np.rint(model.predict(x_test))

"""
#printing the predictions of test data against the real results
print("X\t\t\t Y\tPrediction")
i = 0
for pred in predictions:
    print (x_test[i], '\t', y_test[i], '\t', pred)
    i+=1
"""

#PLOTING

style.use("ggplot")

x_graph = 'G1'
y_graph = 'G3' # the predicted value

plt.scatter(data[x_graph], data[y_graph])
plt.xlabel(x_graph)
plt.ylabel("Predicted Grade")
#plt.show()

NEW_DATA_FILE = "new_Data.csv"
RESULTS_FILE = 'results.txt'
if read_input(NEW_DATA_FILE):    
    new_data = pd.read_csv("new_Data.csv")
    students = np.array(new_data)

    #rounding the prediction to the nearest whole number.
    predictions = np.rint(model.predict(students))

    #printing the predictions against the real results
    i = 0
    for pred in predictions:
        print ("Student " + str(i + 1) + " predicted grade:\t", pred)
        i+=1    
    output(RESULTS_FILE, students, predictions)
    #clear(NEW_DATA_FILE)    
