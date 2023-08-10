"""Gift II"""

def main():
    """Main Function"""

    weight = []
    for _ in range(8):
        weight.append(int(input()))

    for j in range(len(weight)):
        if weight[j]%2 == 0:
            result = weight[j]
            break

    print(result)

main()
