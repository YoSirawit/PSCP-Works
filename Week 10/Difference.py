"""Difference"""

def main():
    """Main Function"""

    num_a = int(input())
    num_b = int(input())

    set_a = set({})
    set_b = set({})

    for _ in range(num_a):
        set_a.add(int(input()))

    for _ in range(num_b):
        set_b.add(int(input()))

    result = set_a - set_b

    print(*sorted(result), sep=" ")

main()
