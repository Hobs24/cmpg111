# using command line arguments using the sys module python
#sys.argv// avgv = argument variable // this variabe is a list 

import sys

#sys.argv its uses list indexing and start at 1, that is where the value you in the command terminal is stored 
try:
    print("Hello, my name is", sys.argv[1])

except IndexError:
    print("Too few arguments")
