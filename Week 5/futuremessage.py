"""future"""

def main():
    """Main Function"""

    sentence = input()

    if sentence.isdecimal():
        print("Number")
    elif sentence.isupper():
        print("Uppercase")
    elif sentence.islower():
        print("Lowercase")
    elif sentence.isspace():
        print("Space")
    elif sentence.istitle():
        print("Title")
    else:
        print("Other")

main()
