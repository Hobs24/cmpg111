#Print the title
print("Interest Calculator\n")

#Create variable to store user input 
b = float(input("Please enter your balance: R"))

#Calculate the interest to two decimal places
interest = f"The final amount is: R{b * 0.06:,.2f}"                     #
print(interest)