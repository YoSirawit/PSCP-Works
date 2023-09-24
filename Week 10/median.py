"""Median"""

def main():
    """Main Function"""

    quantity = int(input())
    num_lst = []

    for _ in range(quantity):
        num_lst.append(int(input()))

    num_lst.sort()

    if quantity % 2 == 0:
        med = (num_lst[(quantity-1)//2] + num_lst[quantity//2]) / 2
    else:
        med = num_lst[quantity//2]

    print("%.1f" %med)

main()
