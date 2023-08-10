"""Point in circle"""

def main():
    """Main Function"""

    cen_x = float(input())
    cen_y = float(input())
    rad = float(input())
    point_x = float(input())
    point_y = float(input())

    if ((point_y-cen_y)**2 + (point_x-cen_x)**2)**0.5 <= rad:
        print("True")
    else:
        print("False")

main()
