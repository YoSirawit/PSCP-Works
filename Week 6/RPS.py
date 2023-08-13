"""Rock Paper Scissors"""

def main():
    """Main Function"""

    action = input()
    a_won = 0
    b_won = 0
    for i in range(0, len(action), 2):
        if i+1 <= len(action):
            a_act = action[i]
            b_act = action[i+1]
            a_wont, b_wont = check(a_act, b_act)
            a_won += a_wont
            b_won += b_wont
    if a_won > b_won:
        print("A win %d-%d" %(a_won, b_won))
    elif b_won > a_won:
        print("B win %d-%d" %(b_won, a_won))
    else:
        print("DRAW %d" %a_won)

def check(a_deci, b_deci):
    """Check if A or B win"""

    a_win = 0
    b_win = 0

    if a_deci == "R" and b_deci == "P":
        b_win = 1
    elif b_deci == "S" and a_deci == "R":
        a_win = 1
    elif a_deci == "P" and b_deci == "S":
        b_win = 1
    elif b_deci == "R" and a_deci == "P":
        a_win = 1
    elif a_deci == "S" and b_deci == "R":
        b_win = 1
    elif b_deci == "P" and a_deci == "S":
        a_win = 1
    elif b_deci == "R" and a_deci == "S":
        b_win = 1
    elif a_deci == "P" and b_deci == "R":
        a_win = 1
    elif b_deci == "P" and a_deci == "R":
        b_win = 1
    elif a_deci == "S" and b_deci == "P":
        a_win = 1
    elif b_deci == "S" and a_deci == "P":
        b_win = 1
    elif a_deci == "R" and b_deci == "S":
        a_win = 1
    return a_win, b_win

main()
