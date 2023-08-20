"""BigFrame"""

def main():
    """Main Function"""

    word_1 = input().strip(" ")
    word_2 = input().strip(" ")
    word_3 = input().strip(" ")
    word_4 = input().strip(" ")
    word_5 = input().strip(" ")

    longest = max(len(word_1), len(word_2), len(word_3), len(word_4), len(word_5))

    print("*"*(longest+4))
    print("*", word_1 + " "*abs(len(word_1)-longest), "*")
    print("*", word_2 + " "*abs(len(word_2)-longest), "*")
    print("*", word_3 + " "*abs(len(word_3)-longest), "*")
    print("*", word_4 + " "*abs(len(word_4)-longest), "*")
    print("*", word_5 + " "*abs(len(word_5)-longest), "*")
    print("*"*(longest+4))

main()
