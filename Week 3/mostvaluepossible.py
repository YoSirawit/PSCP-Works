"""Most value possible"""

def main():
    """Main Function"""

    num_a = int(input())
    num_b = int(input())
    num_c = int(input())

    vala, valb = comyon(str(num_a), str(num_b))
    vala, valc = comyon(vala, str(num_c))
    valb, valc = comyon(valb, valc)

    num_a = str(vala)
    num_b = str(valb)
    num_c = str(valc)

    if num_a[0] == num_b[0] or num_a == num_c[0] or num_b[0] == num_c[0]:
        norma, normb = check(num_a, num_b)
        norma, normc = check(norma, num_c)
        normb, normc = check(normb, normc)
        result = norma+normb+normc
    else:
        result = vala+valb+valc

    print("%d" %int(result))

def comyon(valx, valy):
    """Compare but yon"""
    if valx < valy:
        valx, valy = valy, valx
    return str(valx), str(valy)

def check(valx, valy):
    """Sorting Function"""
    if len(valx) > 1 and len(valy) == 1:
        if valx[1] > valy[0]:
            return valx, valy
        else:
            return valy, valx
    elif len(valy) > 1 and len(valx) == 1:
        if valy[1] > valx[0]:
            return valy, valx
        else:
            return valx, valy
    else:
        return valx, valy

main()
