"""PhoneNumber"""

def main():
    """Main Function"""

    number = input()
    kind = input()

    if kind == "International":
        number = number.replace("0", "+66", 1)
        if len(number) == 11:
            print(number[:3], number[3:7], number[7:])
        elif len(number) == 12:
            print(number[:4], number[4:8], number[8:])
    else:
        if len(number) == 9:
            print(number[0], number[1:5], number[5:])
        else:
            print(number[:2], number[2:6], number[6:])

main()
