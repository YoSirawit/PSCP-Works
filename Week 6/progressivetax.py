"""Progressive Tax"""

def diff(rate, num_diff):
    """calculate tax per stage"""
    if num_diff < 0:
        num_diff = 0
    result = (num_diff * rate)/100
    return result

def main():
    """Main Function"""

    income = int(input())
    tax = diff(5, min(income-150000, 150000)) + diff(10, min(income-300000, 200000)) \
        + diff(15, min(income-500000, 250000)) + diff(20, min(income-750000, 250000)) \
        + diff(25, min(income-1000000, 1000000)) + diff(30, min(income-2000000, 2000000))\
        + diff(35, income-4000000)

    print("%d" %tax)

main()
