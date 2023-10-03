"""Fibonacci V1"""

def main(num):
    """Main Function"""

    result = fibo(num)
    print(result)

def fibo(num):
    """Find result of fibonacci number"""

    if num > 1:
        result = fibo(num-1) + fibo(num-2)
        return result
    elif num == 1:
        return 1
    return 0

main(int(input()))
