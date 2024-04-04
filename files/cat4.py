# when you what get user input, that matches a your expection 
while True:         # keep looping until we get a valid input
    n = int(input("What is n? "))
    if n > 0:       
        break     # exit the loop

for _ in range(n):       
    print("meow")    