"""Rule of three"""

def main():
    """Main Function"""

    num = int(input())
    price_a = float(input())
    size_a = float(input())
    value_a = size_a/price_a

    for _ in range(num-1):
        price_b = float(input())
        size_b = float(input())
        value_b = size_b/price_b
        if value_b >= value_a:
            if price_b >= price_a and value_a == value_b:
                pass
            else:
                price_a = price_b
                size_a = size_b
                value_a = value_b

    print("%.2f %.2f" %(price_a, size_a))

main()
