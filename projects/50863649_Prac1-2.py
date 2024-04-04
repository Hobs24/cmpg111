# Ask the user for a symbol
character = input("Please enter a symbol: ")

#Draw triangle using symbol input
print("\n\nTriangle\n")
n = 5
for i in range(n):
    print(character * (i+1))
