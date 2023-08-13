"""Create N shape"""

def main():
    """This function will create N shape"""

    size = int(input())

    for i in range(size):
        for j in range(size):
            if j == 0 or j == size-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main()
