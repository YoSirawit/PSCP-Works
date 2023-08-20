"""HarshNumber"""

def main():
    """Main Function"""

    for _ in range(10):
        num = int(input())
        digit = str(num)
        p_result = 0
        digit = digit.strip("-")
        if num == 0:
            print("No")
        else:
            for i in digit:
                p_result += int(i)
            if num % p_result == 0:
                print("Yes")
            else:
                print("No")

main()
