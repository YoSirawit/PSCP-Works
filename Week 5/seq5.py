"""SEQ5"""

def main():
    """Main Function"""

    num = int(input())

    while True:
        for _ in range(7):
            print(num, end=" ")
            num -= 1
            if num < 1:
                break
        if num < 1:
            break
        print()

main()
