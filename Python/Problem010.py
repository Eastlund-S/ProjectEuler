"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

intial result 1179908154
new result 894899033
third result 1179908154
fourth result 142913828922 and this one is correct!
trying to use numpy sum must have been causing problems,
easier to just sum the primes as we go
"""

import numpy as np
# from ProblemThree import check_if_prime


def check_if_prime(n):
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    index = 5
    step = 4
    while index < int(np.sqrt(n)) + 1:
        if n % index == 0:
            return False
        step = 6 - step
        index += step
    print(n)
    return True


def find_primes_below_n(n):
    primes = []
    x = 2
    while x < n:
        if check_if_prime(x) is True:
            primes.append(x)
        x += 1
    primes_np = np.array(primes)
    return primes_np


def sum_primes_below_n(n):
    sum_of_primes = 0
    x = 2
    while x < n:
        if check_if_prime(x) is True:
            sum_of_primes += x
        x += 1
    return sum_of_primes


def is_x_one(x):
    """This is equivalent to 'return true'"""
    return x == 1


def main():
    print(sum_primes_below_n(2000000))


if __name__ == '__main__':
    main()
