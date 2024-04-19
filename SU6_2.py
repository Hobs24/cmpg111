# This code displays Programmer's name and student number

first_name = input("Enter your name")
second_name = input("Enter second name")
student_number = input("Enter your student number ")
print('The Programmer is', first_name, second_name, student_number)

import random

def generateRandom():
    random.seed(111)  # Set seed for predictability
    lottery_numbers = random.sample(range(1, 50), 7)
    return sorted(lottery_numbers)

def selectNumbers():
    lottery_numbers = []
    print("Enter seven unique numbers between 1 and 49:")
    while len(lottery_numbers) < 7:
        try:
            number = int(input(f"Enter number {len(lottery_numbers) + 1}: "))
            if 1 <= number <= 49 and number not in lottery_numbers:
                lottery_numbers.append(number)
            else:
                print("Invalid number! Please enter a unique number between 1 and 49.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    return sorted(lottery_numbers)

def displayLottery(numbers):
    print("Lottery numbers:", end=" ")
    for num in numbers:
        print(num, end=" ")

def main():
    lottery_numbers = [0] * 7
    print("Initial list:", lottery_numbers)
    option = input("Select an option - '1' for random generation, '2' for manual selection: ")
    if option == '1':
        lottery_numbers = generateRandom()
    elif option == '2':
        lottery_numbers = selectNumbers()
    else:
        print("Invalid option! Exiting program.")
        return

    displayLottery(lottery_numbers)

if __name__ == "__main__":
    main()
