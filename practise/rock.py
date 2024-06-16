#playing rock, paper scissors with computer
import random
#prompt user and compter for input
user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
computer = random.choice(['r', 'p', 's'])

if user == computer:
    print("Its a tie")
elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
    print("You won!!")
else:
    print("You lost :( Computer won!!")