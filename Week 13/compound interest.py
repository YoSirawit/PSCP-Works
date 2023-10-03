"""Compound Interest"""

def cal(money, rate, time):
    """Calculate money"""

    result = money * (1 + rate/100)**time

    print("{:.2f}".format(result))

cal(int(input()), float(input()), int(input()))
