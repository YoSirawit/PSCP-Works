"""SEQ12"""

def main():
    """Main Function"""

    num = int(input())

    for row in range(num*2 - 1):
        for col in range(num*2 - 1):
            if (row >= num-1 and col <= num-1) or (row <= num-1 and col >= num-1):
                print("%02d" %abs(abs((col + row)-(num-1)*2) - num), end=" ")
            else:
                print("%02d" %abs(abs(row-col)-num), end=" ")
        print()

main()
