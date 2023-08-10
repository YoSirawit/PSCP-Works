""" HowLong """

def main():
    """Main Function"""

    number = int(input())
    result = 0

    while True:
        if abs(number) >= 1:
            result += 1
            number = abs(number/10)
        elif number == 0:
            result += 1
            break
        else:
            break

    print(result)

main()
