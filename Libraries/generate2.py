#shuffle value in a list using the shuffle function in random module in python
import random

#shuffle function only takes in an argument in its parameter not a list, so create a variable list
cards = ["Jack", "Queen", "King", "Bisho"]
random.shuffle(cards)
for card in cards:            #this will print the values in the list in individual line
    print(cards)