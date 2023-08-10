"""Robot I"""

def main():
    """Main Function"""

    name = input()
    age = float(input())

    if age < 18:
        print("{0}, you can pass.".format(name))
    else:
        print("{0}, you shall not pass.".format(name))

main()
