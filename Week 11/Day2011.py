"""Day 2011"""

def day(date, month):
    """Find day in 2011"""
    for i in range(1, month):
        if i == 2:
            date += 28
        elif i in [1, 3, 5, 7, 8, 10]:
            date += 31
        else:
            date += 30

    lst_day = ['Friday', 'Saturday', 'Sunday', 'Monday', \
               'Tuesday', 'Wednesday', 'Thursday']
    print(lst_day[date % 7])

day(int(input()), int(input()))
