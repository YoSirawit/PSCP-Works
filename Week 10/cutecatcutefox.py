"""Cute cat Cute fox"""
import json

def cute(catfoxnum):
    """find quantity of cat and fox"""

    group = {}
    fox = 0
    cat = 0
    group['Garfield'] = 'Cat01'    
    group['Fubuki'] = 'Fox01'

    for _ in range(catfoxnum):
        tmp = input()
        if 'Cat01' in tmp:
            group.pop('Garfield')
        elif 'Fox01' in tmp:
            group.pop('Fubuki')
        group.update(json.loads(tmp))


    lst = list(group.items())
    lst.sort(key=sorting)

    for _ in range(len(lst)):
        if 'Fox' in lst[_][1]:
            fox += 1
        elif 'Cat' in lst[_][1]:
            cat += 1

    print("Cat : {0}\nFox : {1}".format(cat, fox))

    for i, j in lst:
        print(i, ":", j)

def sorting(kind):
    """Sorting"""

    result = kind[1]
    return result

cute(int(input()))
