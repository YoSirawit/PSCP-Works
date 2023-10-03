"""OTP"""

def otp():
    """Check if otp is valid or not"""

    while True:
        num_dct = {}
        num = input().strip(" ")
        if num == "0":
            break
        for i in num:
            if i not in num_dct:
                num_dct[i] = 1
            else:
                num_dct[i] += 1
        result = "Invalid"
        if len(num) == 4:
            value = list(num_dct.values())
            check = value.count(2)
            if check == 1:
                result = "Valid"
            else:
                result = "Invalid"
        else:
            result = check_result(len(num), num_dct)
        print(result)

def check_result(lenght, dct):
    """Check result if it's actually valid"""
    if lenght == 6:
        value = list(dct.values())
        check_a = value.count(2)
        check_b = value.count(3)
        if check_a == 2 or check_b == 1:
            result = "Valid"
        else:
            result = "Invalid"
    elif lenght == 8:
        value = list(dct.values())
        check_a = value.count(2)
        check_b = value.count(3)
        if check_a == 3 or check_b == 2:
            result = "Valid"
        else:
            result = "Invalid"

    return result

otp()
