"""save"""

def main():
    """save"""
    result = 492137954293754252786
    seconds = result//1000
    result = result%1000
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    print(days, hours, minutes, seconds, result)

main()
