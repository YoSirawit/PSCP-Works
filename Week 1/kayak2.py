'''Kayak'''
def main():
    '''Kayak'''
    var_num = int(input())
    weight = input().split()
    count = 0
    total = 0
    for _ in range(var_num * 2):
        weight[_] = int(weight[_])
    weight_sorted = sorted(weight)
    num = weight_sorted[var_num * 2 - 1] ** 2
    for i in range(weight_sorted[var_num * 2 - 1]):
        for j in range(var_num * 2 - 1):
            if weight_sorted[j + 1] - weight_sorted[j] == i:
                count += 1
                total += weight_sorted[j + 1] - weight_sorted[j]
                weight_sorted.pop(j)
                weight_sorted.pop(j)
                weight_sorted.append(num)
                weight_sorted.append(num ** 2)
                j = j - 1
                print(j)
                print(weight_sorted)
        if count == var_num - 1:
            break
    print(total)
main()

