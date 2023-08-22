"""
A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of
two 3-digit numbers.

result = 906609
"""


def check_if_palindrome(array):
    for index in range(0, len(array)):
        if array[index-1] != array[-index]:
            return False  # Not a Palindrome
    return True


def main():
    largest_palindrome = 1
    # Iterate over all possible products
    for x in range(100, 1000):
        for y in range(100, 1000):
            # Prevent wasteful iterations
            if y < x:
                result = x * y
                if check_if_palindrome(str(result)) is True:
                    # Keep a record of the largest value as this is not necessarily
                    # the final value
                    if result > largest_palindrome:
                        largest_palindrome = result
    print(largest_palindrome)


if __name__ == '__main__':
    main()
