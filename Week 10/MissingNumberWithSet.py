"""Missing Number With Set"""

def missingnumber():
    """Find Missing Number"""

    range_num = int(input())
    default = set({})
    for i in range(1, range_num+1):
        default.add(i)

    set_num = set({})
    while True:
        num_add = int(input())
        if num_add == 0:
            break
        set_num.add(num_add)

    print(*sorted(default-set_num), sep="\n")

missingnumber()
