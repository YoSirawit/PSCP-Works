"""Almost Mean"""

def main():
    """Main Function"""

    student_num = int(input())
    student_lst = []
    target_index = 0
    mean = 0

    for _ in range(student_num):
        temp = input().split("\t")
        student_lst.append(temp)
        mean += float(temp[1])

    mean = mean/student_num

    for i in range(1, len(student_lst)):
        com_1 = float(student_lst[target_index][1])
        com_2 = float(student_lst[i][1])
        if (com_1 < com_2 and com_2 <= mean) or (com_2 < com_1 and com_1 > mean):
            target_index = i

    print(student_lst[target_index][0] + "\t" + student_lst[target_index][1])

main()
