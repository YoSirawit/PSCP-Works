"""Ticket Flare"""

def main():
    """Main Function"""

    laststation = int(input())
    firststage = int(input())
    first_price = int(input())
    secondstage = int(input())
    second_price = int(input())
    third_price = int(input())

    start = int(input())
    stop = int(input())
    travel = abs(start - stop)

    if stop > laststation:
        result = "Error"
    elif start == stop and firststage == 0:
        result = third_price
    elif travel > firststage+secondstage:
        result = first_price + secondstage*second_price + \
            (travel - firststage - secondstage)*third_price
    elif travel > firststage:
        result = first_price + (travel - firststage)*second_price
    else:
        result = first_price

    print(result)

main()
