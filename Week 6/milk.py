"""Milk"""

def main():
    """Milk"""

    bottleprice = int(input())
    every = int(input())
    free = int(input())
    money = int(input())
    get = (money//bottleprice)-every
    result = 0

    if free == 0:
        result = money//bottleprice
    else:
        result = ((get//abs(every-free))*free) + every + free + get

    print(result)

main()
