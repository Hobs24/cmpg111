# Ask the user for length values
s1 = int(input("Enter the length of stick #1: "))
s2 = int(input("Enter the length of stick #2: "))
s3 = int(input("Enter the length of stick #3: "))

#Use triangle inequality theorem to check if the sticks can form a triangle
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print("\nTriangle possible")
    if s1 == s2 == s3:
        print("Equilateral triangle possible")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Isosceles triangle possible")
    else:
        print("Scalene triangle possible")

else:
    print("\nNo triangle possible")