"""Encoder"""

def main():
    """Main Function"""

    data = input()
    point = 0
    num = 0

    for i in data:
        if point == 0:
            num += 1
            point += 1
        elif i == data[point-1]:
            num += 1
            point += 1
        else:
            print(str(num) + data[point-1], end="")
            num = 1
            point += 1
        if point == len(data):
            print(str(num) + data[point-1], end="")

main()
