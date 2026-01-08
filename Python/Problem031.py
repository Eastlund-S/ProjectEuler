"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can £2 be made using any number of coins?
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
    # numbers = set()
    # for x in range(2, 1000000):
        # if power_test(x, 5):
            # numbers.add(x)
    numbers = {x for x in range(2, 1000000) if power_test(x, 5)}
    print(sum(numbers))

COINS = {1, 2, 5, 10, 20, 50, 100, 200}

def main():
    """New method using dynamic programming?"""
    target = 200
    ways = set(range(0, target + 1))
    ways_index = []
    for x in ways:
        ways_index.append(0)
    print(ways_index, len(ways_index))
    for coin in COINS:
        for amount in ways:
            if coin < amount:
                pass


if __name__ == '__main__':
    main()
