

print("This game allows you to enter a number, Enter 0 to exit the game.")
num = int(input("Enter any Number: "))

while num != 0:
    if num > 0: 
        print("The number you Entered is a positive number") 
    else:
        print("The number you Entered is a negative number ")
    break
