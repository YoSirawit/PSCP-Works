"""Dart"""

def cal_point(times):
    """Calculate point"""

    point = 0

    for _ in range(times):
        pos = tuple(input().split(" "))
        distance = (int(pos[0])**2 + int(pos[1])**2)**0.5
        if distance <= 2:
            point += 5
        elif distance <= 4:
            point += 4
        elif distance <= 6:
            point += 3
        elif distance <= 8:
            point += 2
        elif distance <= 10:
            point += 1

    print(point)

cal_point(int(input()))
