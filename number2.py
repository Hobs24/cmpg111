# 1. Ask the user for a number
while True:                    # while loop
    try:                                # try block
     x = int(input("What is x? "))

    except ValueError:                 # except block
         print("x is not a integer")

    else:                         # else block
        break

print(f"x is {x}")