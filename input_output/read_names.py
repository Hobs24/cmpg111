#how to read a file

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())#rstrip() this function strips off new line