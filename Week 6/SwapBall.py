"""SwapBall"""

def main():
    """Main Function"""

    action = input()
    cup_a = 1
    cup_b = 0
    cup_c = 0

    for i in action:
        if i == "A":
            cup_a, cup_b = cup_b, cup_a
        elif i == "B":
            cup_b, cup_c = cup_c, cup_b
        elif i == "C":
            cup_a, cup_c = cup_c, cup_a

    if cup_a > 0:
        print("1")
    elif cup_b > 0:
        print("2")
    else:
        print("3")

main()
