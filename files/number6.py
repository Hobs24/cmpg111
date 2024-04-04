def main():                      # main function
    x = get_int("What is x?")                    
    print(f"x is {x}")
    



def get_int(prompt):                      #prompt is a string that will be displayed to the user
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass                          # pass is a null operation, nothing happens when it executes
       
main()