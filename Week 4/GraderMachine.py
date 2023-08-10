""" Grader Machine """

def main():
    """ Main Function """

    start = int(input())
    last = int(input())
    result = 0

    print("pass : ", end="")
    if last >= start:
        if start%2 == 0:
            for i in range(start, last+1, 2):
                result += i
                print(i, end=" ")
        else:
            for i in range(start+1, last+1, 2):
                result += i
                print(i, end=" ")
    else:
        if start%2 == 0:
            for i in range(start, last-1, -2):
                result += i
                print(i, end=" ")
        else:
            for i in range(start-1, last-1, -2):
                result += i
                print(i, end=" ")

    print()
    print("Sum :", result)

main()
