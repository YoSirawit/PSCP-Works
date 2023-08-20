"""Milk"""

def main():
    """Milk"""

    bottleprice = int(input())
    every = int(input())
    free = int(input())
    money = int(input())
    result = money//bottleprice
    get = result

    while get >= every and free != 0:
        if every == 0:
            break
        result += free
        get += free
        get -= every

    print(result)

main()
