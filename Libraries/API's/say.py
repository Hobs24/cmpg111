#use pip, which is python package manager // use it to install packages like cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, "+ sys.argv[1])  #cow function only takes in one string