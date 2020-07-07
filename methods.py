import pandas as pd 
import os
def append(file_path, data):
    with open(file_path, 'a+') as file:
        file.write(data + '\n')
    file.close()
def write(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data + '\n')
    file.close()    

# Delete a file
def clear(file_path):
    if os.path.exists(file_path):
        os.unlink(file_path)

def read_input(NEW_DATA_FILE):
    try:
        number_of_students = int(input("Enter the number of students you want to predict for:\t"))
        
        if number_of_students > 0:
            write(NEW_DATA_FILE, "age,health,freetime,studytime,absences,G1,G2")
        for i in range(number_of_students):
            age = float(input("Enter Student " + str(i + 1) + " age:\t")) 
            health = float(input("Enter Student " + str(i + 1) + " health:\t"))
            freetime = float(input("Enter Student " + str(i + 1) + " freetime:\t"))
            studytime = float(input("Enter Student " + str(i + 1) + " studytime:\t"))
            absences = float(input("Enter Student " + str(i + 1) + " absences:\t"))
            G1 = float(input("Enter Student " + str(i + 1) + " first grade:\t"))
            G2 = float(input("Enter Student " + str(i + 1) + " second grade:\t"))
            line = ''
            line = str(age) + ',' + str(health) + ',' + str(freetime) + ',' + str(studytime) + ',' + str(absences) + ',' + str(G1) + ',' + str(G2)

            append(NEW_DATA_FILE, line)
        return True    
    except Exception as e:
        print("EXCEPTION.\t" + str(e))
        return False        

def output(RESULTS_FILE, students, arr):
    if not os.path.exists(RESULTS_FILE):
        write(RESULTS_FILE, "age,health,freetime,studytime,absences,G1,G2,G3")
    new_data = pd.read_csv("new_Data.csv")
    i = 0
    for l in range(len(students)):
        line = ''
        for j in range(students.shape[1]):
            line += str(students[i][j]) + ','

        line += str(arr[i])
        i+=1
        
        append(RESULTS_FILE, line)

        
