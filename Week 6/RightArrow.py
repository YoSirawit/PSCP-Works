"""RightArrow"""

def right_arrow():
    """Create right arrow"""

    width = int(input())
    height = int(input())
    middle = height // 2

    for i in range(height):
        print(" "*(middle - abs(i - middle)) + "*"*width)

right_arrow()
