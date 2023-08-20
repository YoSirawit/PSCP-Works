"""diginity"""

def main():
    """Main Function"""

    while True:
        num = input()
        if num != "0":
            while True:
                num = loop(num)
                if num < 10:
                    print(num)
                    break
                else:
                    num = str(num)
        else:
            break

def loop(value):
    """plus number in string"""
    result = 0
    for i in range(len(value)):
        result += int(value[i])
    return result

main()
