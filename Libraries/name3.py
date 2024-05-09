
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#supporting many argument at the prompt
for arg in sys.argv[1:]:    #[1:] slices the list, start at element 1 and continues
    print("Hello, my name is", arg)    