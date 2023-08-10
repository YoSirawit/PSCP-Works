"""Align"""
import math

def main():
    """Main Function"""

    size = int(input())
    posi = input()
    sentence = input()

    if posi == "left":
        print("%s" %sentence.ljust(size))
    elif posi == "right":
        print("%s" %sentence.rjust(size))
    else:
        space = math.ceil((size - len(sentence))/2)
        print(" "*space + sentence)

main()
