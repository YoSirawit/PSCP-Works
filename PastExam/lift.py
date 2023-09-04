"""Lift"""

def main():
    """Main Function"""

    people = int(input())
    cap_weight = float(input())
    weight = 0
    status = "Safe"
    last_age = 0

    for _ in range(people):
        age = int(input())
        weight += float(input())
        if last_age < 12:
            last_age = age
        if last_age >= 12:
            status = "Safe"
        else:
            status = "Not Safe"

    if weight > cap_weight:
        status = "Not Safe"

    print(status)

main()
