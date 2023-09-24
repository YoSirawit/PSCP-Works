"""ISprimeSmall"""

def main():
    """Main Function"""

    result = "Yes"
    num = int(input())
    if num == 1:
        result = "No"
    else:
        for i in range(2, int((num**0.5)+1)):
            if num % i == 0 and num != 2:
                result = "No"
                break
    print(result)
main()
