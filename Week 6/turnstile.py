"""Turnstile"""

def main():
    """Main Function"""
    state = "lock"
    pass_num = 0

    while True:
        action = input()
        if action == "C" and state == "lock":
            state = "unlock"
        elif action == "P" and state == "unlock":
            state = "lock"
            pass_num += 1
        elif action == "END":
            break

    print(pass_num)

main()
