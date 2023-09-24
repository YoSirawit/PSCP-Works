"""Coin Changer V1"""

def coin(money):
    """Coin Changer"""

    allcoins = [25, 10, 5, 1]

    result = 0

    for i in range(4):
        result += money // allcoins[i]
        money -= (money // allcoins[i]) * allcoins[i]

    print(result)

coin(int(input()))
