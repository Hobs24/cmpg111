try:                 # try to do something
    x = int(input("What is x? "))
    print(f"x is {x}")

except ValueError:             # if there is a ValueError, do this
    print("x is not a integer")