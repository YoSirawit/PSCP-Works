"""Check if valid variable name"""

def main():
    """Check valid var name"""

    volumn = int(input())
    lst = ["if", "else", "elif", "while", "for", "True", "False", "continue", "break", "return", \
           "is", "in", "and", "or", "from", "as", "pass", "not", "def", "None"]

    for _ in range(volumn):
        var = input()
        if var.isidentifier() and not var in lst:
            print("Valid")
        else:
            print("Invalid")

main()
