import pandas as pd 
import numpy as np

d = pd.read_csv('new_Data.csv')
print(d)
print("\n\n")
students = np.array(d)
j = 0
for l in range(len(students)):
        line = ''
        print(students.shape[1])
        for i in range(students.shape[1]):
            #if i == 
            line += str(students[j][i]) + ','
        print(line)
        j+=1