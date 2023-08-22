"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

answer is 6857
"""

import numpy as np

VALUE = 600851475143


def get_factors(n):
    factors = []
    limit = int(np.sqrt(n))

    for x in range(2, limit):
        if VALUE % x == 0:
            factors.append(x)
    print(factors)
    print(len(factors))
    return factors

# Old an inefficient
# def check_if_prime(n):
#     prime_flag = []
#     index = n
#     while index > 1:
#         if n % index == 0:
#             prime_flag.append(index)
#         index -= 1
#     if len(prime_flag) == 1:
#         return True


# # New and more efficient method
# def check_if_prime(n):
#     index = 2
#     while index < n:
#         if n % index == 0:
#             return False
#         index += 1
#     return True

# Even newer and more efficient method
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


def main():
    # Find factors
    factors = get_factors(VALUE)

    # Find if factor is prime. There is probably a more pleasant way than
    # what I have done to keep a record of if a factor is prime. I find
    # the prime flag method as more of a hack, but it works.
    prime_factors = []
    for x in factors:
        if check_if_prime(x) is True:
            prime_factors.append(x)
    print(prime_factors)


if __name__ == '__main__':
    main()
