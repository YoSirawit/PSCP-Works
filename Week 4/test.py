def main(start, stop):
    num_sum = 0
    num_pass = ""
    step = 1
    if start > stop:
        stop -= 1
        step = -1
    for i in range(start, stop+1, step):
        if i%2 == 0:
            num_pass += "%d " %i
            num_sum += i
    print("pass : %s\nSum : %d" %(num_pass, num_sum))
main(int(input()), int(input()))