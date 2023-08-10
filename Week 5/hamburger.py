"""Hamburger"""

def main():
    """Main Function"""

    leftbun = int(input())
    rightbun = int(input())

    print("|"*leftbun + "*"*((leftbun+rightbun)*2) + "|"*rightbun)

main()
