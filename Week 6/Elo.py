"""ELO"""

def main():
    """Main Function"""

    rating_a = int(input())
    rating_b = int(input())
    want_result = input()

    if want_result == "A":
        print("%.2f" %possibility(rating_b, rating_a))
    else:
        print("%.2f" %possibility(rating_a, rating_b))

def possibility(rate_1, rate_2):
    """Calculate possibility"""
    result = (1/(1+10**((rate_1 - rate_2)/400)))
    return result

main()
