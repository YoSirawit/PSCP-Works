"""Left Arrow"""

def main():
    """Create Left Arrow"""

    width = int(input())
    height = int(input())

    for i in range(height):
        print(" "*abs(i - (height//2)) + "*"*width)

main()
