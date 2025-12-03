"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) =b and d(b) =a, where a ≠𝑏, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110;
therefore d(220) =284. The proper divisors of 284 are 1,2,4,71 and 142; so d(284) =220.

Evaluate the sum of all the amicable numbers under 10000.

31626

What I learned from doing this:

- Using set() is a good way to make a list and automatically check for duplicates.
- smart checking logic is better than looping an entire list!
"""

import numpy as np

def proper_divisors_sum(n):
    proper_divisors = []
    for divisor in range(n-1, 0, -1):
        if n % divisor == 0:
            proper_divisors.append(divisor)
    p_d = np.asarray(proper_divisors)
    p_d_sum = p_d.sum()

    return int(p_d_sum)

def main():
    amicable_number_list = set()
    test_range = 10000

    for number in range(1, test_range):
        p_d_sum = proper_divisors_sum(number)
        if (proper_divisors_sum(p_d_sum) == number
            and number < test_range
            and number != p_d_sum):
            print(f"{number} corresponds to {p_d_sum}")
            amicable_number_list.add(number)
    amicable_numbers = sorted(amicable_number_list)
    print(f"Amicable numbers are {amicable_numbers  }")
    print(f"Sum of these is {sum(amicable_numbers)}")

    # for number in range(2, test_range):
        # _, p_d_sum = proper_divisors(number)
        # amicable_test_list = []

        # _, num = proper_divisors(int(p_d_sum))
        # _, num_sum = proper_divisors(int(num))

        # if ((num_sum == number)
            # and num != number
            # and num_sum < test_range):
            # amicable_number_list.add(number)
            # amicable_number_list.add(num)
    # result = sorted(amicable_number_list)
    # print(f"amical numbers below {test_range}: {result}")
    # print(f"sum is {sum(result)}")

        # for num in range(int(p_d_sum) + 1):
            # amicable_test_list.append(num)
            # _, amicable_test_sum = proper_divisors(num)
            # if amicable_test_sum == number:
                # # print(f"Amicable numbers {num}, {number}")
                # if num not in amicable_number_list:
                    # amicable_number_list.append(num)
                # if number not in amicable_number_list:
                    # amicable_number_list.append(number)
        # print(f"Proper divisors of {number} are {p_d_list}, sum to {p_d_sum}")
        # print(amicable_test_list)
    # print(f"Amical numbers below {test_range} are {amicable_number_list}")
    # sum_of_amicables = np.asarray(amicable_number_list)
    # print(f"Sum of amicables is {sum_of_amicables.sum()}")


if __name__ == '__main__':
    main()
