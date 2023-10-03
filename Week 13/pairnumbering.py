"""PairNumbering"""
import json

def pair():
    """Find how many pair"""

    a_lst = json.loads(input())
    b_lst = json.loads(input())
    want = int(input())

    a_dct = {}
    b_dct = {}

    total = 0

    for i in a_lst:
        if i > want:
            continue
        if want - i in b_lst and i not in a_dct.keys():
            a_dct[i] = a_lst.count(i)
            b_dct[want - i] = b_lst.count(want - i)

    for j in a_dct.keys():
        total += a_dct[j] * b_dct[want - j]

    print(total)

pair()
