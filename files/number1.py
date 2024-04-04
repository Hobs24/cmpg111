try:                                # try block
    x = int(input("What is x? "))

except ValueError:                 # except block
    print("x is not a integer")

else:                             # else block
    print(f"x is {x}")