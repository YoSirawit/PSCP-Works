"""LastStand"""
import json

def main():
    """Main Function"""

    all_num = json.loads(input())
    last_digit = []

    for i in all_num:
        last_digit.append(str(i)[-1])

    for i in last_digit:
        print(i)

main()
