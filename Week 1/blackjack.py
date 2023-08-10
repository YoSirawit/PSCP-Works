"""BlackJack"""

def main():
    """Main Function"""

    volume = int(input())
    memmo = 0
    value = 0
    for _ in range(volume):
        card = input()
        if card.isdecimal():
            value += int(card)
        elif card.lower() == "a":
            memmo += 1
            value += 0
        else:
            value += 10

    if memmo > 0:
        for _ in range(memmo):
            value += 11
            if value > 21:
                value -= 10
    if memmo > 1 and value > 21:
        value -= 10

    print(value)

main()
