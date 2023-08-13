"""Ball"""

def cal_bounce():
    """Caluculate how many times that ball was bounces"""

    height = float(input())
    times = 0

    while True:
        height /= 1.66666666666666666666
        if height < 0.01:
            break
        else:
            times += 1

    print(times)

cal_bounce()
