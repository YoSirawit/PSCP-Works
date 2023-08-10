"""grade3"""
import math

def main():
    """Main Function"""

    subject = int(input())
    result = 0

    for _ in range(subject):
        score = grade(float(input()))
        result += score

    result = math.floor((result / subject) * 100) / 100

    print("%.2f" %result)

def grade(point):
    """return grade"""

    if 95 <= point <= 100:
        result = 4
    elif 90 <= point < 95:
        result = 3.5
    elif 85 <= point < 90:
        result = 3
    elif 80 <= point < 85:
        result = 2.5
    elif 75 <= point < 80:
        result = 2
    elif 70 <= point < 75:
        result = 1.5
    elif 65 <= point < 70:
        result = 1
    elif 60 <= point < 70:
        result = 0.5
    else:
        result = 0
    return result

main()
