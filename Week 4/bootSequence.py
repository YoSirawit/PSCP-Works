""" Boot Sequence """

def main():
    """Main function"""

    stop = int(input())

    for i in range(1, stop):
        print(i, end="_")
    print(stop)

main()
