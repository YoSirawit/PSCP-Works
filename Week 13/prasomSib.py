"""PrasomSib"""

def main(num):
    """Main Function"""

    times = 0

    for i in range(len(num)):
        tmp = int(num[i])
        for j in range(i+1, len(num)):
            tmp += int(num[j])
            if tmp == 10:
                times += 1
                break
            elif tmp > 10:
                break

    print(times)

main(input())
