#ask user for name and house and tell where user is from harry potter world
#tuple type of data that is a collection of values but u can't change value inside

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)               #tuple

if __name__=="__main__":
    main()