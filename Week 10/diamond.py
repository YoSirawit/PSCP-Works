"""Diamond"""

def main(depth, width):
    """Main Function"""

    price_lst = []

    for _ in range(width):
        price_lst.append(0)

    for _ in range(depth):
        price_inp = input().split(" ")
        for j in range(width):
            price_lst[j] += int(price_inp[j])

    price_lst.sort(reverse=True)

    print(price_lst[0])

main(int(input()), int(input()))
