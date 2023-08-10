"""Function"""

def main():
    """Main Function"""
    inp_a = float(input())
    inp_b = float(input())
    inp_c = float(input())
    inp_d = float(input())

    value1 = func_g(func_f(inp_d**2))

    print(func_f(func_f(inp_a)))
    print(func_g(func_f(inp_a - inp_b)))
    print(func_h(func_f(inp_a+inp_b), func_f(inp_a+inp_c), value1))
    print(func_i(func_h(func_f(inp_a+inp_b), func_f(inp_a-inp_c), value1)\
                 , func_g(func_f(inp_a-inp_b))\
                    , func_f(func_f(func_f(func_f(func_f(inp_c)))))\
                        , inp_d**8))

def func_f(num_x):
    """F Function"""
    result = 2 * num_x
    return result

def func_g(num_x):
    """G Function"""
    result = (3*(num_x**4)) - (num_x**3) + (2*(num_x**2)) + 10
    return result

def func_h(num_x, num_y, num_z):
    """H Function"""
    result = (num_z + num_x)**2 - (num_x*num_y) + (num_y**2)
    return result

def func_i(num_a, num_b, num_c, num_d):
    """I Function"""
    result = (num_a**2 + num_b**2 - num_c**2) / (num_d**2 - (2*num_a*num_d) + (2*num_a))
    return result

main()
