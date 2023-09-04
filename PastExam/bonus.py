"""Bonus"""

def main():
    """Main Function"""

    salary = int(input())
    years = int(input())
    months = int(input())

    if months >= 10:
        years += 1

    bonus = max(min(min((salary * years), (salary * 20)), 1000000), 5000)

    print(bonus)

main()
