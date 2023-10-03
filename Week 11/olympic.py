"""Olympic"""

def main(countries):
    """Main Function"""

    leaderboard = {}
    rank = 1
    previous_rank = 1
    previous_score = ("0", "0", "0")

    for _ in range(countries):
        tmp = input().split(" ")
        leaderboard[tmp[0]] = (tmp[1], tmp[2], tmp[3])

    lst = list(leaderboard.items())
    lst.sort()
    lst.sort(key=medals, reverse=True)

    for i in lst:
        if i[1] == previous_score:
            print(previous_rank, i[0], i[1][0], i[1][1], i[1][2], calscore(i[1]))
            rank_use = previous_rank
        else:
            print(rank, i[0], i[1][0], i[1][1], i[1][2], calscore(i[1]))
            rank_use = rank

        previous_score = i[1]
        previous_rank = rank_use
        rank += 1

def medals(score):
    """Return to check medals"""
    return score[1]

def calscore(allmedals):
    """Calculate all medals"""
    result = int(allmedals[0]) + int(allmedals[1]) + int(allmedals[2])
    return result

main(int(input()))
