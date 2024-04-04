def main():
    x = get_int()
    print(f"x is {x}")
    



def get_int():
    while True:
        try:
         x = int(input("What is x? "))            # it will return the value of x and exit the loop
        except ValueError:
            print("x is not a integer")
        else:
            return x
                    

main()                              