"""Password"""
import math as m

def main():
    """Main Function"""

    password = input()

    haslower = 0
    hasupper = 0
    hasprintable = 0
    hasnumber = 0

    for i in password:
        if i.islower():
            if haslower == 0:
                haslower = 1

        elif i.isupper():
            if hasupper == 0:
                hasupper = 1

        elif i.isdigit():
            if hasnumber == 0:
                hasnumber = 1

        elif i.isprintable():
            if hasprintable == 0:
                hasprintable = 1

    pool = 26*haslower + 26*hasupper + 10*hasnumber + 32*hasprintable
    entropy = m.floor(m.log(pool**len(password), 2))

    print(entropy)
    print(status(entropy))

def status(bit):
    """Check how strong password is"""

    if bit < 28:
        result = "Very Weak"
    elif bit < 36:
        result = "Weak"
    elif bit < 60:
        result = "Reasonable"
    elif bit < 128:
        result = "Strong"
    else:
        result = "Very Strong"

    return result

main()
