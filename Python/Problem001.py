"""If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Sum is 233168"""

import numpy as np


def main():
    multiples = []
    i = 0
    for x in range(1, 1000):
        if x % 3 == 0:
            multiples.append(x)
            i += 1
        elif x % 5 == 0:
            multiples.append(x)
            i += 1
    # I don't want to read all these numbers!
    # print(multiples)
    multiples = np.array(multiples)
    sum_of_multiples = np.sum(multiples)
    print(sum_of_multiples)


if __name__ == '__main__':
    main()
