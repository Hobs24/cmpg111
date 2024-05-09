def calcAverage(test_scores):
    return sum(test_scores) / len(test_scores)

def determineGrade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    test_scores = []
    for i in range(5):
        score = float(input(f"Enter test score {i+1}: "))
        test_scores.append(score)
    
    average_score = calcAverage(test_scores)
    grade = determineGrade(average_score)
    
    print(f"\nAverage Test Score: {average_score}")
    print(f"Letter Grade: {grade}")


main()
