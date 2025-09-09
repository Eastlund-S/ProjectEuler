"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

Answer: 232792560
"""


def check_if_divisible(number):
    for x in range(2, 21):
        if number % x != 0:
            return False
    return True


def lcm(a, b):
    result = (a * b)/gcd(a, b)
    return result


def gcd(a, b):
    while 1 == 1:
        if a == b:
            return a
        if a > b:
            a = a - b
        else:
            b = b - a


def main():
    current_lcm = lcm(2, 1)
    for x in range(3, 21):
        current_lcm = lcm(x, current_lcm)
    print(current_lcm)
    # I wrote this earlier so may as well use it!
    print(check_if_divisible(current_lcm))


if __name__ == '__main__':
    main()
