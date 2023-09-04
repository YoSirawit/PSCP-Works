"""Pringles"""

def main():
    """Main Function"""

    upper_can = input()
    inside = input()
    under_can = input()
    finger_long = int(input())
    eat = 0

    for i in range(len(inside)):
        if inside[i] == ")" and i < finger_long:
            eat += 1
            inside = inside.replace(")", " ", 1)
        elif i >= finger_long:
            break

    print(eat)
    if inside.count(")") == 0:
        print("None.")
        print(upper_can)
        print(inside)
        print(under_can)
    else:
        print("There are still some left.")
        print(upper_can)
        print(inside)
        print(under_can)

main()
