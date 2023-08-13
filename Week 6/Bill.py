""""Bill"""

def bill():
    """Calculate price"""

    price = int(input())

    p_service = price * 0.1
    p_service = max(p_service, 50)
    p_service = min(p_service, 1000)

    price += p_service
    vat = price * 0.07

    total = price + vat

    print("%.2f" %total)

bill()
