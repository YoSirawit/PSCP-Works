"""BMI Again"""

def main():
    """Main Function"""
    score = bmi()
    if score < 18.5:
        print("Underweight")
    elif score < 25:
        print("Normal")
    elif score < 30:
        print("Overweight")
    else:
        print("Obese")

def bmi():
    """Calculatebmi"""

    weight = int(input())
    height = int(input())
    result = weight / ((height/100)**2)

    return result

main()
