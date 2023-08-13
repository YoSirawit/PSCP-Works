"""SEQ X"""

def main():
    """Create box with X in the middle by number that input"""

    size = int(input())
    volumn = int(input())

    for i in range(size):
        for _ in range(volumn):
            for k in range(size):
                if i == k or k == 0 or k == size-1 or i+k == size-1 or \
                    i == 0 or i == size-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        print()

main()
