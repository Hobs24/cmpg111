import random


def guess():


     random_num = random.randint(1, 100)
     guesses = 0

    while True:
     num = int(input("Guess a number (0 to quite): "))
     guesses += 1

     if num == 0:
        break
                                        
     elif num < random_num:
          print("Too low, Try again")

     elif num > random_num:
          print("Too high,Try again")

     else:
          print(f"Congratulations! you guessed the number {num} correctly in {guesses} guesses.")
          break


guess()  