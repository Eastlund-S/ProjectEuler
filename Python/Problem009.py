"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

answer = 31875000
"""

import numpy as np


def find_special_triplet(x):
    result = 0
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            c_squared = (a*a) + (b*b)
            c = np.sqrt(c_squared)
            print(a, b, c)
            if a < b:
                if b < c:
                    if (a*a) + (b*b) == (c*c):
                        if (a + b + c) == 1000:
                            result = (a * b * c)
                            return result
    print("Need to increase range!")
    return result


def main():
    x = 1000
    result = find_special_triplet(x)
    print(result)


if __name__ == '__main__':
    main()
