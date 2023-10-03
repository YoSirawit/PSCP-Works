"""MatrixMN"""

def mat(row, column):
    """Matrix"""
    lst_col = []
    lst_row =[]

    for _ in range(row):
        for _ in range(column):
            lst_col.append(int(input()))
        lst_row.append(lst_col)
        lst_col = []

    for i in range(len(lst_row)):
        print(*lst_row[i])

mat(int(input()), int(input()))
