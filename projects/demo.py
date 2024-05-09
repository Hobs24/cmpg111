# Function to calculate the total sum of five numbers
def calcTotal(num1, num2, num3, num4, num5):
    total = num1 + num2 + num3 + num4 + num5
    return total


# Function to calculate the average of a total sum
def calcAverage(total):
    return total / 5


# Function to determine the highest value among five numbers
# Note: Using multiple if statements to handle cases where multiple numbers may have the same highest value
def determineHighest(num1, num2, num3, num4, num5):
    highest = num1

    if num1 > num2:
        highest = num2
    if num2 > num3:
        highest = num3
    if num3 > num4:
        highest = num4
    if num5 > num1:
        highest = num5

    return highest


# Void function to check if the highest value is even or odd and print a message accordingly
def checkEvenOdd(highest):
    if highest % 2 == 0:
        print("The highest value is even.")
    else:
        print("The highest value is odd.")


# Main function to execute the program
def main():
    # Input values from the user
    value1 = int(input("Enter value 1: "))
    value2 = int(input("Enter value 2: "))
    value3 = int(input("Enter value 3: "))
    value4 = int(input("Enter value 4: "))
    value5 = int(input("Enter value 5: "))

    # Calculate total sum
    total = calcTotal(value1, value2, value3, value4, value5)
    # Calculate average
    average = calcAverage(total)
    # Determine highest value
    highest = determineHighest(value1, value2, value3, value4, value5)

    # Output results
    print("\nTotal:", total)
    print("Average:", average)
    print("Highest:", highest)
    # Check if the highest value is even or odd
    checkEvenOdd(highest)


# Entry point of the program
if __name__ == "__main__":
    main()