"""Letters Frequency"""

def letters(sentence):
    """Find letter frequency in sentence"""

    sentence_lower = sentence.lower()
    previous = 0
    current = 0
    for i in range(97, 123):
        current = sentence_lower.count(chr(i))
        if current >= previous:
            previous = current
            letter = chr(i)

    print(letter)


letters(input())
