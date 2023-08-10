"""timing"""

def main():
    """timing"""
    second = int(input())
    minute = second//60
    second = second%60
    hours = minute//60
    minute = minute%60
    days = hours//24
    hours = hours%24
    if days <= 9999 and second >= 0:
        print("%04d:%02d:%02d:%02d" %(days, hours, minute, second))
    elif days > 9999 or second < 0:
        print("ERR_:__:__:__")

main()
