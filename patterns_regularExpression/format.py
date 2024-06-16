import re

# formating user's name in the order we expect

#creating variable to store user's name
#:= it allows you to asign a value from right to left and ask a boolean question about
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): 
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")