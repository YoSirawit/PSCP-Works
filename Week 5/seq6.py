"""SEQ6"""

def main():
    """Main Function"""

    num = int(input())
    default = 1

    for _ in range(num):
        for i in range(1, default+1):
            print(i, end=" ")
        default += 1
        print()

main()
