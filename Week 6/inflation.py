"""Inflation"""
import math as m

def main():
    """Main Function"""

    money = float(input())
    years = int(input())
    rate = 0.0381

    for _ in range(years):
        money += money*rate
    money = money// 100
    print("%.2f" %money)

main()
