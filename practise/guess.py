#guessing game 

import random

# generate a random number between 1 and 100
random_num = random.randint(1, 100)

guess_num = 0

while random_num != guess_num:
    #prompt user to geuss the random number
    guess_num = int(input("Guess a random number between 1-100: "))

    if guess_num < random_num:
        print("The number you guessed is too low") 
    elif guess_num > random_num: 
        print("The number you guessed is too high")
        
print("Congrats!!! You guessed the correct number :)")