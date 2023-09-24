"""PickThemAgain"""

def main():
    """Main Function"""

    all_num = input().split(" ")
    new_lst = []

    for i in all_num:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            new_lst.append(i)

    new_lst.reverse()

    if len(new_lst) != 0:
        for i in new_lst:
            print(i)
    else:
        print("Nope")

main()
