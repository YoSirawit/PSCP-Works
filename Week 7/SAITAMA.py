"""Saitama"""
import math as m

def compare(value_a, value_b):
    """Compare two value and return most"""
    if value_a < value_b:
        return value_b
    else:
        return value_a

def find(num_a, num_b):
    """Find days that use to complete task"""
    return m.ceil(num_a/num_b)

def main():
    """Main Function"""

    pushup = int(input())
    situp = int(input())
    squad = int(input())
    running = int(input())
    pushup_can = int(input())
    situp_can = int(input())
    running_can = int(input())
    squad_can = int(input())

    days = compare(compare(compare(find(pushup, pushup_can), find(situp, situp_can)), \
                    find(running, running_can)), find(squad, squad_can))

    print(days)

main()
