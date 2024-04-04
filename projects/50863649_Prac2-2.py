#Import math to pi
import math
#Print title 
print("Circle Calculations\n")

#prompt user to enter radius of circle
rad = int(input("Enter radius of circle: "))

c = round(2 * math.pi * rad, 2)
a =round(math.pi * rad * rad, 2)

print("\nThe circumference of circle is: ", c)
print("The area of the circle is: ", a)

h = int(input("\nPlease enter the height of the cylinder: "))

v =round(math.pi * rad * rad * h, 2)

print("\nThe volume of the cylinder is: ", v)