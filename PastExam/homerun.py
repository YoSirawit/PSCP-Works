"""HomeRun"""

def main():
    """Main Function"""

    court = int(input())
    far = float(input())
    result = 0

    for _ in range(court):
        size = float(input())
        if far > size:
            result += 1

    print(result)

main()
