"""Duplicate1"""

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

    set_c = set_a.intersection(set_b)

    if len(set_c) != 0:
        print(*sorted(set_c, reverse=True), sep="\n")
    else:
        print("Nope")

main()
