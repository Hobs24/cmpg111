import random

def generateRandom():
    return [random.randint(1, 49) for _ in range(7)]

def selectNumbers(numbers):
    for i in range(7):
        while True:
            try:
                num = int(input(f"Enter lottery number {i+1} (1-49): "))
                if num < 1 or num > 49:
                    print("Number must be between 1 and 49.")
                elif num in numbers:
                    print("Number already chosen. Please select a different number.")
                else:
                    numbers[i] = num
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    numbers = [0] * 7
    print(f"Initial list: {numbers}")
    while True:
        choice = input("Select an option - '1' for random numbers, '2' for manual selection: ")
        if choice == '1':
            numbers = generateRandom()
            break
        elif choice == '2':
            selectNumbers(numbers)
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    print(f"Final list of lottery numbers: {numbers}")

if __name__ == "__main__":
    main()
