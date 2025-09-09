"""
Starting in the top left corner of a 2x2 grid, and only
being able to move to the right and down, there are
exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import math


def main():
    size_of_grid = 20
    n = 2 * size_of_grid
    k = size_of_grid
    # This problem is solved by doing a binomial distribution of ( n )
    #                                                            ( k )
    # where n is x + y and k is x
    number_of_routes = (math.factorial(n)) / ((math.factorial(k))*(math.factorial(n - k)))
    print(number_of_routes)


if __name__ == '__main__':
    main()
