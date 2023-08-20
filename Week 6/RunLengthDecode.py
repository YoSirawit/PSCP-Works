"""Decoding"""

def main():
    """Main Function"""

    data = input()
    num = ""

    for i in data:
        if i.isdigit():
            num += i
        else:
            print(i*int(num), end="")
            num = ""

main()
