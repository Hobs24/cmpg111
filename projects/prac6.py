import random

def generateRandom():
    random.seed(111)                   
    lottery_numbers = random.sample(range(1, 50), 7)
    return sorted(lottery_numbers)

def selectNumbers(numbers_list):
    selected_numbers = []

    while len(selected_numbers) < 7:                     #len = length of list
        try:
            number = int(input(f"Enter number {len(selected_numbers) + 1}: "))
            if 1 <= number <= 49 and number not in selected_numbers:
                selected_numbers.append(number)
            else:
                print("Please enter a valid and unique number between 1 and 49.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return sorted(selected_numbers)

def displayLottery(numbers_list):
    print(*numbers_list, sep=" ")

def main():
    lottery_numbers = [] 
    print(lottery_numbers)
    option = input("Select an option - 1: Generate random lottery numbers, 2: Select lottery numbers manually: ")
    if option == "1":
        lottery_numbers = generateRandom()
    elif option == "2":
        lottery_numbers = selectNumbers(lottery_numbers)
    else:
        print("Invalid option selected. Exiting program.")
        return

    displayLottery(lottery_numbers)

if __name__ == "__main__":
    main()
