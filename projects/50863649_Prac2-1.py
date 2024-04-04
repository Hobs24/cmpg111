#Title 
print("Python Calculator")

#Prompt user for two nembers
x = int(input("\nPlease enter the first number: "))
y = int(input("Please enter the second number: "))
print("\n")

#Display different calculations based on user input
a1 = x + y
a2 = x - y
a3 = x * y
a4 = x / y
a5 = x // y
a6 = x % y

#Print the sum and answers
print(x, "+", y, "=" ,a1)
print(x, "-", y, "=" ,a2)
print(x, "*", y, "=" ,a3)
print(x, "/", y, "=" ,a4)
print(x, "//", y, "=" ,a5)
print(x, "%", y, "=" ,a6)