#using open() function to open a file
name = input("What's your name? ")

#open() return a file handle which need to be stored in a variable
file = open("names.txt", "a") # a is a second argument that allows you to append in the file
file.write(f"{name}\n")       #w is an argument that allows  you to write in the file
file.close() #closes the file