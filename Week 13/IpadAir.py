"""iPad Air"""

def cal_cost(color, cap, feature):
    """Calculate cost of iPad"""

    all_color = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    want = set()

    if color in all_color:
        if cap == 64 or cap == 256:
            want.add(cap)
        if feature == "Wi-Fi" or feature == "Wi-Fi + Cellular":
            want.add(feature)

    if len(want) == 2:
        if want == {64, "Wi-Fi"}:
            cost = 19900
        elif want == {64, "Wi-Fi + Cellular"}:
            cost = 24400
        elif want == {256, "Wi-Fi"}:
            cost = 24900
        else:
            cost = 29400
    else:
        cost = "Not Available"

    print(cost)

cal_cost(input(), int(input()), input())
