"""Triangle"""

def main():
    """Main Function"""

    length_1 = float(input())
    length_2 = float(input())
    length_3 = float(input())

    if length_1 > length_2 and length_1 > length_3:
        result = check(length_1, length_2, length_3)
    elif length_2 > length_1 and length_2 > length_3:
        result = check(length_2, length_1, length_3)
    else:
        result = check(length_3, length_1, length_2)
    print(result)

def check(diag, side1, side2):
    """Check if possible to create triangle"""

    if abs(diag**2 - ((side1**2) + (side2**2))) <= 0.01:
        return "Yes"
    else:
        return "No"

main()
