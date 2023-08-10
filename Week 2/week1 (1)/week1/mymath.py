"""Mymath"""

import math as m

def main():
    """Main Function"""
    num_a = (m.sin(m.radians(90)) + (m.sin(m.radians(60)))**2) / (m.cos(m.radians(245**2)) \
    + m.cos(m.radians(45+135)))
    num_b = (m.factorial(16) * m.factorial(4)) / m.factorial(8)
    num_c = (15 + 25) / (((25-12)**2) + ((12 - 15)**2))**0.5
    num_d = m.log10(1234**4)
    num_e = (m.log(4234, 5) + m.log2(8191) + (71 * (m.log10(156154))))\
    / (m.log(777, 7) - m.log(888, 8) - m.log(999, 9))

    print(num_a)
    print(num_b)
    print(num_c)
    print(num_d)
    print(num_e)

main()
