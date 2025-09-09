"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.

Answer: 25164150
"""


def sum_of_squares_up_to_n(n):
    sum_of_squares = 0
    for x in range(1, n + 1):
        sum_of_squares += x*x
    return sum_of_squares


def square_of_sum_up_to_n(n):
    sum_of_x = 0
    for x in range(1, n + 1):
        sum_of_x += x
    square_of_sum = sum_of_x * sum_of_x
    return square_of_sum


def difference_between_two_numbers(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def main():
    print(sum_of_squares_up_to_n(100))
    print(square_of_sum_up_to_n(100))
    print(difference_between_two_numbers(sum_of_squares_up_to_n(100),
                                         square_of_sum_up_to_n(100)))


if __name__ == '__main__':
    main()
