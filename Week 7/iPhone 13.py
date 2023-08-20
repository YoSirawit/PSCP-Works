"""Iphone 13"""

def set_price(size_want, price_a, price_b, price_c, price_e):
    """Set price of model"""
    if size_want == "128 GB":
        price = price_a
    elif size_want == "256 GB":
        price = price_b
    elif size_want == "512 GB":
        price = price_c
    elif size_want == "1 TB":
        price = price_e
    else:
        price = "Not Available"
    return price

def main():
    """Main Function"""

    model = input()
    cap_size = input()

    if model == "iPhone 13 mini":
        print(set_price(cap_size, 25900, 29900, 37900, "Not Available"))
    elif model == "iPhone 13":
        print(set_price(cap_size, 29900, 33900, 41900, "Not Available"))
    elif model == "iPhone 13 Pro":
        print(set_price(cap_size, 38900, 42900, 50900, 58900))
    elif model == "iPhone 13 Pro Max":
        print(set_price(cap_size, 42900, 46900, 54900, 62900))
    else:
        print("Not Available")

main()
