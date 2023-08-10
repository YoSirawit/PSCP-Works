"""virus1"""

def main():
    """Main Function"""

    virus = input()
    num = 0

    for i in virus:
        if i == "o":
            num += 1

    print(num)
main()
