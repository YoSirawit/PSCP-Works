"""Rectangle Area"""

def main(a_tangle, b_tangle):
    """Main Function"""

    left_da = (a_tangle[0], a_tangle[1])
    left_ua = (left_da[0], left_da[1] + a_tangle[3])
    right_da = (left_da[0] + a_tangle[2], left_da[1])
    right_ua = (left_da[0] + a_tangle[2], left_da[1] + a_tangle[3])

    left_db = (b_tangle[0], b_tangle[1])
    left_ub = (left_db[0], left_db[1] + b_tangle[3])
    right_db = (left_db[0] + b_tangle[2], left_db[1])
    right_ub = (left_db[0] + b_tangle[2], left_db[1] + b_tangle[3])

    all_pos_a = [left_ua, left_da, right_ua, right_da]
    all_pos_b = [left_ub, left_db, right_ub, right_db]

    if left_da <= left_db < right_da:
        area = (right_da[0] - left_db[0]) * (left_ub[1] - left_db[1])
        

main(list(map(int ,input().split(" "))), list(map(int, input().split(" "))))
