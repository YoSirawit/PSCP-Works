"""Allprimes"""

def main(lastnum):
    """Main Function"""

    primes = 0
    for i in range(1, lastnum+1):
        if isprime(i) == 'Yes':
            primes += 1

    print(primes)

def isprime(num):
    """Main Function"""

    result = "Yes"
    if num == 1:
        result = "No"
    else:
        for i in range(2, int((num**0.5)+1)):
            if num % i == 0 and num != 2:
                result = "No"
                break

    return result

main(int(input()))
