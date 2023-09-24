"""Point Sorting"""

def point(test):
    """Point Sorting"""

    for _ in range(test):
        lst = []
        point_num = int(input())
        for _ in range(point_num):
            tmp = tuple(input().split(" "))
            tmp = (int(tmp[0]), int(tmp[1]))
            lst.append(tmp)
        lst.sort()
        lst.sort(key=sorting)
        for i in lst:
            print(i[0], i[1])

def sorting(num_a):
    """Calculate"""
    return num_a[0] + num_a[1]

point(int(input()))
