def main():                      # main function
    x = get_int()
    print(f"x is {x}")
    



def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass                          # pass is a null operation, nothing happens when it executes
       
main()