""" Arrow """
def main():
    """ Arrow """
    width = int(input())
    height = int(input())
    for i in range(height):
        print(" "* abs((height//2)-i) + "*"*width)
main()
