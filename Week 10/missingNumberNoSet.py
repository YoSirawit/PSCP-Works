"""Missing Numbet but no set"""

def main():
    """Main Function"""

    lst_num = []
    donthave = []

    times = int(input())
    while True:
        num = int(input())
        if num == 0:
            break
        elif num not in lst_num:
            lst_num.append(num)

    for i in range(1, times+1):
        if i not in lst_num:
            donthave.append(i)

    donthave.sort()
    print(*donthave, sep="\n")

main()
