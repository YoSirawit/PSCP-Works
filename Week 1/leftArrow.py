"""Left arrow"""

def main():
    """Main Function"""

    width = int(input())
    height = int(input())
    mid = height // 2

    for i in range(height):
        print(" " * abs(mid - i) + "*" * width)

main()
