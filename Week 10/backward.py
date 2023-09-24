"""Backward"""

def main():
    """Main Function"""

    word_lst = []
    while True:
        word = input()
        if word != "NULL":
            word_lst.append(word)
        else:
            break

    word_lst.reverse()
    for i in word_lst:
        print(i)

main()
