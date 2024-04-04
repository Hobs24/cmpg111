def main():                      # main function
    x = get_int()
    print(f"x is {x}")
    



def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            print("x is not a integer")
       
main()