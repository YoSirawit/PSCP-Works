"""AscendingSort"""

def main():
    """Main Function"""

    asc = []
    for _ in range(5):
        asc.append(int(input()))

    asc.sort()
    for i in asc:
        print(i)

main()
