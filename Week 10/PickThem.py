"""PickThem"""
import json

def main():
    """Main Function"""

    all_num = json.loads(input())
    even = []

    for i in all_num:
        if i % 2 == 0:
            even.append(i)

    if len(even) != 0:
        for i in even:
            print(i)
    else:
        print("Nope")

main()
