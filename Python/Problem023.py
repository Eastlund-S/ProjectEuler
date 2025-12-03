"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 +2 +4 +7 +14 =28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 +2 +3 +4 +6 =16, the smallest number
that can be written as the sum of two abundant numbers is 24. By mathematical
analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

4179871

Learned:
More about using sets - this is great!

Things to take forward:
Try to optimise by using sqrt - need to investigate this
Understand list comprehension

"""

def proper_divisors(n):
    proper_divisors = set()
    for divisor in range(n-1, 0, -1):
        if n % divisor == 0:
            proper_divisors.add(divisor)
    p_d = sorted(proper_divisors)
    p_d_sum = sum(p_d)

    return p_d, p_d_sum

def main():
    abundant_number_list = set()
    for number in range(int(28123)):
        p_d, p_d_sum = proper_divisors(number)
        if p_d_sum > number:
            abundant_number_list.add(number)
        # print(f"proper divisors of {number} are {p_d}, summing to {p_d_sum}")

    # Trying to do the same thing as above but with list comprehension
    # _, abundant_number_list = [proper_divisors(number) for number in range(28123) if proper_divisors(number)[1] > number]

    """
    all_numbers_list = set()
    for x in range(28124):
        all_numbers_list.add(x)
    """
    all_numbers_list = set(range(28124))

    for number_1 in abundant_number_list:
        for number_2 in abundant_number_list:
            if (number_1 + number_2) in all_numbers_list:
                all_numbers_list.discard(number_1 + number_2)
    
    abun_numbers_sum = sum(sorted(all_numbers_list))
    print(abun_numbers_sum)




if __name__ == '__main__':
    main()
