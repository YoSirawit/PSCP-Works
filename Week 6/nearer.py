"""Nearer"""

def near():
    """Check who nearer"""

    alice = int(input())
    bob = int(input())
    car = int(input())

    if abs(car - alice) > abs(car - bob):
        print("Bob %d" %abs(car - bob))
    elif abs(car - alice) < abs(car - bob):
        print("Alice %d" %abs(car-alice))
    else:
        print("Sundaes %d" %abs(car - alice))

near()
