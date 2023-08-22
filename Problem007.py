"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

104743, but not by the fastest possible method
"""

import numpy as np
# from ProblemThree import check_if_prime


def check_if_prime(n):
    index = 2
    while index < int(n / 2) + 1:
        if n % index == 0:
            return False
        index += 1
    return True


def find_nth_prime(n):
    primes = []
    x = 2
    while len(primes) < (n + 1):
        if check_if_prime(x) is True:
            print(x)
            primes.append(x)
        x += 1
    return primes[(n - 1)]


def main():
    print(find_nth_prime(10001))


if __name__ == '__main__':
    main()
