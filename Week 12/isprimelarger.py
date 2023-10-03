"""ISprimeLargeer"""

def main():
    """Main Function"""

    result = "True"
    num = int(input())
    if num == 1 or (num % 2 == 0 and num != 2):
        result = "False"
    else:
        for i in range(3, int((num**0.5)+1), 2):
            if num % i == 0:
                result = "False"
                break
    print(result)
main()
