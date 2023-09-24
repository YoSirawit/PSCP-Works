"""Word Sequence I"""

def word():
    """Word Sequence"""

    text = input()
    for i in range(1, len(text)+1):
        print(text[:i])

word()
