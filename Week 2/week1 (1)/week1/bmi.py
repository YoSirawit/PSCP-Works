"""BMI"""

def main():
    """Main"""
    bmi()
    bmi()
    bmi()
    bmi()
    bmi()

def bmi():
    """Calculatebmi"""
    name = input()
    weight = float(input())
    height = float(input())
    result = weight / ((height/100)**2)
    print("%s's  BMI = %.2f" %(name, result))

main()
