"""
Euler discovered the remarkable quadratic formula:

n^2 +n +41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤𝑛 ≤39. However, when n =40,40^2 +40 +41 =40(40 +1) +41 is
divisible by 41, and certainly when n =41,41^2 +41 +41 is clearly divisible by
41.

The incredible formula n^2 -79n +1601 was discovered, which produces 80 primes
for the consecutive values 0 ≤𝑛 ≤79. The product of the coefficients, -79 and
1601, is -126479.

Considering quadratics of the form:

n^2 +an +b, where |a| <1000 and |b| ≤1000

where |n| is the modulus/absolute value of n
e.g. |11| =11 and |-4| =4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n =0.
"""

from math import ceil, sqrt

def is_prime(number):
    if number < 0:
        number = -number
    lim = ceil(sqrt(number)) + 1
    for x in range(2, lim):
        if (number % x) == 0:
            return False
    return True

def main():
    max_n = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 1
            while True:
                quad = n**2 + (a * n) + b
                if is_prime(quad):
                    n += 1
                else:
                    if n > max_n:
                        max_n = n
                        coefficients = (a, b)
                    break
    print(coefficients) 
    print(coefficients[0] * coefficients[1])


if __name__ == '__main__':
    main()
