"""Christmas tree"""

def tree():
    """Create chrismastree"""

    leaf = int(input())
    trunk = int(input())

    for i in range(leaf):
        for j in range(leaf*2 - 1):
            if j == leaf-1 or (i+j >= leaf-1 and j < leaf-1) or (abs(i-j) <= leaf-1 and j > leaf-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for _ in range(trunk):
        print(" "*(leaf-2) + "-"*3)

tree()
