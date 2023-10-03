"""inverter"""

def invert(bit):
    """Invert bit"""

    newbit = ""

    for i in bit:
        if i == "1":
            newbit += "0"
        else:
            newbit += "1"

    print(newbit.lstrip("0"))

invert(input())
