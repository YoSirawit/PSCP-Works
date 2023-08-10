"""Surprise Vote"""

def main():
    """Main Function"""

    score = float(input())
    most = float(input())
    score_left = score - most

    if (score_left == 0 and most <= 2) or most == 2:
        print("Not surprising")
    elif score_left - most <= 0:
        print("Surprising")
    elif abs((score_left - most) - most) <= 2:
        print("Not surprising")
    else:
        print("Surprising")
main()
