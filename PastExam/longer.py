"""Longer"""
import math as m

def main():
    """Main Function"""

    radius = float(input())
    side_a = float(input())
    side_b = float(input())

    rec = (side_a + side_b)*2
    circle = m.pi * 2 * radius

    if rec > circle:
        print("Rectangle is longer")
        print("%.5f" %(rec - circle))
    elif circle > rec:
        print("Circle is longer")
        print("{:.5f}".format(circle - rec))
    else:
        print("Equal")
        print("{:.5f}".format(circle - rec))

main()
