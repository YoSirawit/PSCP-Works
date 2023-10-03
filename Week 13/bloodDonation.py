"""Blood Donation"""

def main(age, weight, times):
    """Main Function"""
    approve = "True"

    if age == 17 or 60 <= age <= 70:
        approve = input()

    if approve == "True":
        if 17 <= age <= 70 and weight >= 45:
            if times == 0 and age < 55:
                print("Yes")
            elif times > 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

main(int(input()), int(input()), int(input()))
