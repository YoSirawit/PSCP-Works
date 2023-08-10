"""Time1"""

def main():
    """Main Function"""

    time = int(input())
    minute = time // 60
    hours = minute//60
    days = hours//24
    seconds = time % 60
    print("%d %d %d %d" %(days, hours%24, minute%60, seconds))

main()
