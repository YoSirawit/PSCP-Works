"""Seconds converter"""

def convert():
    """Convert Time"""

    time = int(input())
    has_second = int(input())
    has_minute = int(input())
    has_hour = int(input())

    second = time
    minute = second // has_second
    second = second % has_second
    hour = minute // has_minute
    minute = minute % has_minute
    hour = hour % has_hour

    print("%d:%d:%d" %(hour, minute, second))

convert()
