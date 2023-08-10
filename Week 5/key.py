"""Key"""

def main():
    """Main Function"""

    num = input()

    result_1 = 0

    for i in num:
        result_1 += int(i)

    result_2 = int((num[10]) + (num[11]) + (num[12])) * 10
    result_3 = str(result_1 + result_2)

    if len(result_3) > 4:
        for j in range(1, 5):
            print(result_3[j], end="")
    elif len(result_3) <= 3:
        result_3 = int(result_3)
        result_3 += 1000
        print(result_3)
    else:
        print(result_3)

main()
