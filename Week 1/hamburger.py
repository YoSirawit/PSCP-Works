"""How big is your HAMBURGER?"""

def main():
    """Main Function"""

    under_bun = int(input())
    top_bun = int(input())
    meat = (under_bun + top_bun) * 2

    print("|" * under_bun + "*" * meat + "|" * top_bun)

main()
