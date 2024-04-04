name = input("What is your name? ")

match name:                    #match keyword is used to compare the value of name with the cases
    
    case "Harry" | "Hermione" |"Ron": #multiple cases can be combined usind | operator
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                          #default case if there is no match
        print("Who??")    
    