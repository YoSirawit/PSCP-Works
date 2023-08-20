"""Parallelogram"""

def main():
    """Main Function"""

    sentence = input()
    for i in range(len(sentence)):
        for j in range(len(sentence)):
            if j >= (len(sentence)-1)-i:
                print(sentence[0:i+1], end="")
                break
            else:
                print(" ", end="")
        print()

    for k in range(1, len(sentence)):
        print(sentence[k:])

main()
