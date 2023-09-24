"""Line Sorting"""

def main():
    """Main Function"""

    num_sentence = int(input())
    sen_lst = []

    for _ in range(num_sentence):
        sen_lst.append(input().strip(" "))

    sen_lst.sort(key=len)
    print(*sen_lst, sep="\n")

main()
