""" Blackjack """
def main():
    """ Blackjak """
    orange = int(input())
    summary = 0
    for _ in range(orange):
        kaoma = input()
        if kaoma == "J" or kaoma == "Q" or kaoma == "K":
            summary += 10
        elif kaoma == "A":
            if summary + 11 > 21:
                summary += 1
            else:
                summary += 11
        else:
            kaoma = int(kaoma)
            summary += kaoma
    print(summary)

main()

# case A = 1
# kaoma > 21 
# case A = 11
# kaoma <= 21
