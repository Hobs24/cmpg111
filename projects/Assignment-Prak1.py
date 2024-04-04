#Prompt user for their name and surname
name = input("Enter your name? ")
surname =input("Enter your surname? ")

#Remove space before, after user's name and surname also capitalize user's name and surname
name = name.strip().title()
surname = surname.strip().title()

#If user multiple names ony use first name
first, last = name.split(" ")

print("This program was written by: " + first, surname )

print("Square ")
shape1 = 