"""Cha Cha Cha"""
import math as m

def main():
    """Main Function"""

    day = int(input())
    money = 0

    for _ in range(day):
        hours = m.ceil(float(input()))
        money += hours*8720

    print(money)

main()
