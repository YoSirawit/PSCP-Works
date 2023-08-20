"""Stamps"""

def main():
    """Check how much this customer actually paid"""

    times = int(input())
    every_pay = int(input())
    get_stamp = int(input())
    every_stamps = int(input())
    discount_perxstamps = int(input())
    stamps = 0
    total = 0

    for _ in range(times):
        if every_stamps == 0:
            canuse = stamps
        else:
            canuse = stamps // every_stamps

        bill = int(input())

        for _ in range(canuse):
            bill -= discount_perxstamps
            stamps -= every_stamps
            if bill <= 0:
                bill = 0
                break

        if every_pay != 0:
            stamps += (bill // every_pay) * get_stamp
        else:
            stamps += bill * get_stamp

        total += bill

    print(total)
    print(stamps)

main()
