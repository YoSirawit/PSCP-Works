"""math for it"""

def main():
    """math for it"""
    import math
    radius = float(input())
    area = (math.pi)*(radius**2)
    circumference = 2*math.pi*radius
    print("Area:", '%.3f' % area)
    print("Circumference:", '%.3f' % circumference)

main()
