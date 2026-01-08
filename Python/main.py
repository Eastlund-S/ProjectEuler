"""
Main holder for project Euler solutions for Python.main
"""

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
    """
    pass

if __name__ == "__main__":
    problem_31()
