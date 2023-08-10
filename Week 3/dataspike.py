"""DataSpike"""

_DATA = [int(input()), int(input()), int(input()), int(input()), int(input())\
         , int(input()), int(input()), int(input())]

def main():
    """Main Function"""
    ans = check(7)
    print(ans)
def check(num):
    """Find most value varieble"""

    if num >= 0 :
        if _DATA[num] >= check(num-1) :
            result = _DATA[num]
            print(result)
    else:
        result = 0
    return result

main()
