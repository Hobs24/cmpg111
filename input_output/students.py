

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")     #split() fuction can split on any character in a line and it returns value in a list
        print(f"{row[0]} is in {row[1]}")

##############################################################################################################################################

with open("students.csv") as file:
    for line in file:
        #here using name and house we unpack the list because be know the split function give two value from the left and right of the comma
        name, house = line.rstrip().split(",")     #split() fuction can split on any character in a line and it returns value in a list
        print(f"{name} is in {house}")


##########################################################################################################################################
#Try to greet any specific person from the list of students however not in the order they are in example greet Ricce first

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

################################################################################################################################################
#using dictionaries


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #syntx below creates keys (name and house) inside the dictianary
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

#sorting the list in a dictionary using the key parameter

for student in sorted(students, key= get_name):
    print(f"{student['name']} is in {student ['house']}")


###############################################################################################################################################

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #syntx below creates keys (name and house) inside the dictianary
        student = {"name": name, "house": house}
        students.append(student)

#sorting the list in a dictionary using the key parameter
""" here lambda is a psuedo function that takes in a parameter students and returns the value of name of the list od students
and is the as the get_name() function from the code above"""

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in {student ['house']}")

###############################################################################################################################################

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)              #reader() reads csv file, like where are the quotes, commas etc
    for name, home in reader:              #iterating through reader
        students.append({"name": name, "home": home})


#sorting the list in a dictionary using the key parameter
""" here lambda is a psuedo function that takes in a parameter students and returns the value of name of the list od students
and is the as the get_name() function from the code above"""

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in {student ['house']}")


################################################################################################################################################

#writing in a csv file

import csv

name = input("What's your name: ")
home = input("What's your home: ")

with  open("students.csv") as file:
    writer  = csv.DictWriter(file, fieldnames = ["name", "home"]) 
    #second arguments(fieldnames) to DictWriter() write the name of colounms in the first line
    writer.writerrow({"name": name, "home": home})
