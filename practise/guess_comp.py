#Here we ask the compter to guess a number that we provided

import random 



comp_guess = random.randint(1, 100)
feedback  = 0

while comp_guess != feedback:

    feedback = input(f"Is {comp_guess} to high(A), to low (B) or correct (C) ")

    if feedback == 'a' :
        comp_guess = random.randint( 1, comp_guess - 1,)

    elif feedback == 'b':
        comp_guess = random.randint(comp_guess + 1, 100 )
    elif feedback == 'c':
        break
        
print("Computer guessed the number correctly")