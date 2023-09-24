"""Easy Histogram"""

def main():
    """Main Function"""

    lst = []
    sentence = tuple(input())
    sentence = list(sentence)
    for i in sentence:
        volume = sentence.count(i)
        if (i, volume) not in lst and i != " ":
            lst.append((i, volume))
    lst.sort(reverse=True)
    lst.sort(key=low)
    for i in range(len(lst)):
        print(lst[i][0], "=", lst[i][1])

def low(inp):
    """lower the letters"""
    result = inp[0]
    result = (result.lower(), inp[1])
    return result

main()
