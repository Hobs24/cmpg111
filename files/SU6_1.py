
def main():
    numbers = []

    for i in range(0, 20):
        num = int(input("Enter your 20 numbers: "))
        numbers.append(num)

    lowest = determineLowest(numbers)
    highest = determineHighest(numbers)
    total = determineTotal(numbers)
    average = determineAverage(numbers, total)

    print(f"The lowest number is {lowest}")
    print(f"The Highest number is {highest}")
    print(f"the total is {total}")
    print(f"The average is {average}")


def determineHighest(numbers):

    highest = numbers[0]
    for i in numbers:
        if i > highest:
            highest = i
    return highest


def determineLowest(numbers):

    lowest = numbers[0]
    for i in numbers:
        if i < lowest:
            lowest = i
    return lowest


def determineTotal(list):

    total = sum(list)
    return total


def determineAverage(list, total):

    average = total / len(list)
    return average


main()
