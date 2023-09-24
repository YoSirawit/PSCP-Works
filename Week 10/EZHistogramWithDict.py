"""Easy Histogram but with dict"""

def main():
    """Main Function"""

    sentence = input()
    dct = {}

    for i in sentence:
        if i != " ":
            dct[i] = dct.get(i, 0) + 1

    lst = sorted(dct.items(), reverse=True)
    lst.sort(key=low)
    for i, j in lst:
        print(i, "=", j)

def low(inp):
    """lower the letters"""
    result = inp[0]
    result = (result.lower(), inp[1])
    return result

main()
