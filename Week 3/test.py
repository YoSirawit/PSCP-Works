def main():
    print(food(0))

def food(num):
    times = num
    count = 0
    if times < 24:
        chicken = int(input())
        if 50 <= chicken <= 70:
            count = 1 + food(times + 1)
        else:
            count = 0 + food(times + 1)
        return count
    else:
        return count

main()
