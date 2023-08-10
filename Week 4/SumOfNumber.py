""" Sum Of Num """

def main():
    """Main Function"""

    want = int(input())
    result = 0

    while result != want:
        value = int(input())

        if value != -1:
            result += value
        else:
            break

    print(result)

main()
