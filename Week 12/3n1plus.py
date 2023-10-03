"""3n1 Plus"""

def reckon():
    """Count number quantity"""

    while True:
        num = int(input())
        if num == 0:
            break
        else:
            total = 0
            while True:
                if num % 2 == 0:
                    num = num / 2
                    total += 1
                elif num == 1:
                    total += 1
                    break
                else:
                    num = (num * 3) + 1
                    total += 1
            print(total)

reckon()
