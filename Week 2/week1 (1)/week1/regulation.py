"""regulation"""

def main():
    """regulation"""
    aaa = int(input())
    bbb = float(input())
    ccc = str(input())
    print(str(aaa).rjust(30))
    print("%030d" %aaa)
    print('%.2f'%bbb)
    print('%.12f'%bbb)
    print(ccc.rjust(40))

main()
