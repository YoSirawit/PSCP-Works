"""Lotto"""

def main():
    """Check how much you get"""

    prize_1 = input()

    prize_last_2 = input()
    prize_front_3 = [input(), input()]
    prize_last_3 = [input(), input()]
    lotto = input()
    reward = 0

    if prize_1 == "999999":
        near = ["999998", "000000"]
    elif prize_1 == "000000":
        near = ["000001", "999999"]
    else:
        near_t = int(prize_1)+1
        near_1 = "%06d" %near_t
        near_t = int(prize_1)-1
        near_2 = "%06d" %near_t
        near = [near_1, near_2]

    if lotto == prize_1:
        reward += 6000000
    elif lotto in near:
        reward += 100000
    if lotto[4:6] == prize_last_2:
        reward += 2000
    if prize_front_3[0] == prize_front_3[1]:
        if lotto[0:3] in prize_front_3:
            reward += 8000
    else:
        if lotto[0:3] in prize_front_3:
            reward += 4000
    if prize_last_3[0] == prize_last_3[1]:
        if lotto[3:6] in prize_last_3:
            reward += 8000
    else:
        if lotto[3:6] in prize_last_3:
            reward += 4000

    print(reward)

main()
