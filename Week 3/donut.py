"""Donut"""

def main():
    """Main Function"""

    costpiece = int(input())
    freecon = int(input())
    freenum = int(input())
    want = int(input())

    aldy_have = (want // (freecon + freenum)) * (freecon + freenum)
    need = want - aldy_have

    if need >= freecon and freecon + freenum >= need:
        cost = (freecon * costpiece) + ((freecon * (want // (freecon + freenum))) * costpiece)
        total = freecon + freenum + aldy_have
    elif need >= 0:
        cost = (need * costpiece) + ((freecon * (want // (freecon + freenum))) * costpiece)
        total = need + aldy_have
    else:
        cost = ((freecon * (want // (freecon + freenum))) * costpiece)
        total = aldy_have

    print(cost, total)

main()
