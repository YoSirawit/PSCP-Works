"""Devide 3 or 5"""
import math as m

def main(num):
    """Main Function"""

    result = 0

    for i in range(1, m.floor(num)+1):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    print(result)

main(float(input()))
