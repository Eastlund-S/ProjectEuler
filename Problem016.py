"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import numpy as np


def main():
    number = 2 ** 1000
    sum_of_digits = 0
    for x in str(number):
        sum_of_digits += int(x)
    print(sum_of_digits)


if __name__ == '__main__':
    main()
