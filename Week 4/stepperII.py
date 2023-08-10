""" Stepper II """

def main():
    """ Main Function"""

    start = int(input())
    stop = int(input())

    if stop >= start:
        for i in range(start, stop+1):
            print(i)
    else:
        for i in range(start, stop-1, -1):
            print(i)

main()
