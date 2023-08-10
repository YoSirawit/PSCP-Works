"""Brick"""

def main():
    """Main Function"""

    small = int(input())
    large = int(input())
    goal = int(input())

    if goal // 5 >= large:
        goal = goal - (5*large)
    else:
        goal = goal - ((goal // 5)*5)

    if goal <= small:
        print(goal)
    else:
        print("-1")
main()
