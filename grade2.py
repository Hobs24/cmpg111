#asking user for their score and grading them
score = int(input("Score: "))

#pyhton allows you to chain/join to arguments
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif  score >= 70:
    print("Grade: C")
elif  score >= 60:
    print("Grade: D")
else:
    print("Grade: F")