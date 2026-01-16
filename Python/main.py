"""
Main holder for project Euler solutions for Python.main
"""

import cProfile
from datetime import datetime
from fractions import Fraction
from itertools import permutations
from math import ceil, factorial, sqrt

def problem_29():
    terms = {a**b for a in range(2,101) for b in range(2,101)}
    print(len(sorted(terms)))

def power_test(number, power):
    result = 0
    for digit in str(number):
        result += int(digit)**power
    if result == number:
        return True
    else:
        return False

def problem_30():
    numbers = {x for x in range(2, 1000000) if power_test(x, 5)}
    print(sum(numbers))

def problem_31():
    """My solution to Problem 31

    In the United Kingdom the currency is made up of pound (£) and pence (p).
    There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:

    1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
    How many different ways can £2 be made using any number of coins?
    """

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    ways = list(range(0, target + 1))
    print(ways)
    ways_index = []
    for x in ways:
        ways_index.append(0)
    # print(ways_index, len(ways_index))
    ways_index[0] = 1
    for coin in coins:
        for amount in ways:
            if coin <= amount:
                ways_index[amount] += ways_index[amount-coin]
    print(ways_index)

def is_pandigital(number: str) -> bool:
    """Takes a string of numbers and confirms if it's pandigital."""
    if not number.isdigit():
        # print(f"Error: {number} includes non number character.")
        return False
    if "0" in number:
        # print(f"{number} contains a 0.")
        return False

    number_set = set(number)
    # print(f"Received string {number}, converted to set {number_set}")

    if len(number) == len(number_set):
        for char in number:
            if int(char) > len(number):
                return False
        return True
    else:
        return False

def problem_32():
    """We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
    1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum.

    45228

    This could be improved by using itertools permutations to only interate
    over pandigital values. <- I did this and it is so much faster.
    """
    product_list = set()
    # for number in range(123456789, 987654321):
    for num in permutations('123456789'):
        str_num = ''.join(num)
        # number = int(str_num)
        # str_num = str(number)
        if is_pandigital(str_num):
            for prod_break in range(2, (len(str_num)//2)+2):
                for mult_break in range(1, prod_break):
                    # print(str_num[:mult_break], str_num[mult_break:prod_break], str_num[prod_break:])
                    if (int(str_num[:mult_break])
                        * int(str_num[mult_break:prod_break])
                        == int(str_num[prod_break:])):
                        product_list.add(int(str_num[prod_break:]))
                        print(f"Adding {str_num[prod_break:]} from {str_num}")
    print(sum(product_list))

def problem_33():
    """My solution to problem 33.

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
    attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
    correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.

    100
    """
    # numerators = [(a, b) for a in range(0, 10) for b in range(0, 10)]
    # denominators = [(a, b) for a in range(0, 10) for b in range(0, 10)]
    # for numerator in numerators:
        # for denominator in denominators :
            # print(f"{numerator}/{denominator}")
    res_num = 1
    res_den = 1
    for numerator in range(1, 100):
        str_numer = str(numerator).zfill(2)
        if '0' in str_numer:
            continue 
        for denominator in range(1, 100):
            str_denom = str(denominator).zfill(2)
            if (numerator > denominator
                or '0' in (str_denom or str_numer)
                or numerator == denominator):
                continue
            # print(f"{str_numer[0]}/{str_denom[1]}")
            result = None
            if str_numer[0] == str_denom[0]:
                result = int(str_numer[1]) / int(str_denom[1])
            elif str_numer[1] == str_denom[0]:
                result = int(str_numer[0]) / int(str_denom[1])
            elif str_numer[0] == str_denom[1]:
                result = int(str_numer[1]) / int(str_denom[0])
            elif str_numer[1] == str_denom[1]:
                result = int(str_numer[0]) / int(str_denom[0])
            if result:
                if result == (numerator / denominator):
                    res_num *= numerator
                    res_den *= denominator
                    print(f"{numerator}/{denominator}")
    print(f"{res_num}/{res_den}")
    print(f"{Fraction(res_num, res_den)}")

def problem_34():
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are not included.

    40730
    """

    result_sum = 0
    number = 3
    start = datetime.now()
    while (datetime.now() - start).total_seconds() < 60:
    # for number in range (3, 20000000):
        factorial_sum = 0
        for digit in str(number):
            factorial_sum += factorial(int(digit))
        if factorial_sum == number:
            print(number)
            result_sum += number
        number += 1
    print(number)
    print(result_sum)

def is_prime(number: int) -> bool:
    """Tests if a number is a prime number."""
    if number == 2:
        return True
    if number < 0:
        number = -number
    lim = ceil(sqrt(number)) + 1
    for x in range(2, lim):
        if (number % x) == 0:
            return False
    return True

def is_circular_prime(number: int) -> bool:
    """Tests if a number is circular and prime"""
    list_num = list(str(number))
    for index in range(len(list_num)):
        first_digit = list_num.pop(0)
        list_num.append(first_digit)
        cycle_number = int(''.join(list_num))
        if not is_prime(cycle_number):
            return False
    return True

def problem_35():
    """My solution for problem_35

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below : 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
    73, 79, and 97.

    How many circular primes are there below one million?

    55
    """
    circular_primes = set()
    circular_primes.add(2)
    for number in range(2, 1000001):
        if is_circular_prime(number):
            circular_primes.add(number)
            # print(number)
    print(len(circular_primes))

def palindrome(to_check: str) -> bool:
    """Checks if a string is a palindrome and returns a boolean value"""
    string = str(to_check)
    reversed_str = string[::-1]
    if string == reversed_str:
        return True
    return False

def problem_36():
    """My solution for problem_36
    
    The decimal number, 585 == 1001001001 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)

    872187
    """
    palindromic = set()
    for number in range(1, 1000000):
        binary_num = bin(number)
        # print(f"It is {palindrome(str(number))} that number {number} is a palindrome.")
        # print(f"It is {palindrome(str(binary_num)[2:])} that number {binary_num} is a palindrome.")
        if palindrome(str(number)):
            if palindrome(str(binary_num)[2::]):
                palindromic.add(number)
    print(sum(palindromic))

def iterate_truncations(number):
    """Returns a list of possible left/right truncations for a given number"""
    str_number = str(number)
    truncatable_iterations = []
    for index, value in enumerate(str_number):
        test_number_left = str_number[index:]
        if test_number_left is not None:
            truncatable_iterations.append(int(test_number_left))
        test_number_right = str_number[:-(index + 1)]
        if test_number_right != '':
            truncatable_iterations.append(int(test_number_right))
    return truncatable_iterations

def problem_37():
    """My solution for problem 37
    
    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
    left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

    """
    number = 3797
    final_sum = 0
    index = 1
    for number in range(9137, 739397):
        failed = False
        # print(iterate_truncations(number=number))
        for iteration in iterate_truncations(number=number):
            if not is_prime(iteration):
                failed = True
                break
        if not failed:
            print(f"{number} is the {index}th truncatable prime")
            final_sum += number
            index += 1
    print(final_sum)


if __name__ == "__main__":
    # cProfile.run('problem_35()')
    problem_37()
