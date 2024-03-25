# using if statement 
num = int(input("Enter a number between 0 and 100: "))

if (num > 0 and num <100):
    print("The number is within range")

    if(num>=75):
        print("Congrets, you got a distinction! :)")
    elif(num<75 and num>=50):
        print("You passed")
    else:
        print("You failed")


else:
    print("The number is Not within range. Please let your number be between 0 and 100!!!")