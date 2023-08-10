"""SEQ4"""

def main():
    """Main Function"""

    num = int(input())
    default = 1

    for _ in range(num):
        for _ in range(num):
            print(default, end=" ")
            default += 1
        print()

main()
