"""SEQ11"""

def main():
    """Main Function"""

    num = int(input())

    for i in range(2*num - 1):
        for j in range(2*num - 1):
            print("%02d" %abs(max(abs(j-(num-1)), abs(i-(num-1)))-num), end=" ")
        print()

main()
