"""BadKeyBoard"""

def main():
    """Main Function"""

    sentence = input()
    sentence_fix = ""

    for i in sentence:
        if i == "i":
            sentence_fix += "o"
        elif i == "o":
            sentence_fix += "i"
        elif i == "I":
            sentence_fix += "O"
        elif i == "O":
            sentence_fix += "I"
        else:
            sentence_fix += i

    print(sentence_fix)

main()
