"""Niwarn World"""
import math as m

def main():
    """Main Function"""

    n_value = float(input())
    s_value = float(input())
    k_value = float(input())

    print("X: {0:.1f}, Y: {1:.1f}, Z: {2:.1f}".format(x_func(n_value), \
                y_func(n_value, s_value), z_func(k_value)))

def x_func(n_var):
    """Function to find x position"""

    result = 2 + (m.log(n_var**2, 2)/((2*n_var)*m.log(n_var, 2)))
    return result

def y_func(n_var, s_var):
    """Function to find y position"""

    result = (m.sin(m.radians(30))+m.sqrt(2*s_var))/(x_func(n_var)+3)
    return result

def z_func(k_var):
    """Function to find z position"""

    result = (y_func(k_var, k_var)**2)+((8456 * (x_func(k_var)**4))/(24*k_var))
    return result

main()
