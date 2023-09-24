"""Tuple Sad Life"""

def main():
    """Main Function"""

    num_input = tuple(input().split(" "))
    find = input()

    target_position = num_input.index(find)

    for _ in range(num_input.count(find)):
        for _ in range(num_input.count(find)):
            print(target_position, "", end="")
        print()

main()
