"""
If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in
compliance with British usage.

21124
"""

import numpy as np


def check_digit(n):
    if str(n)[-1] == '0':
        return 0
    elif str(n)[-1] == '1':
        return len('one')
    elif str(n)[-1] == '2':
        return len('two')
    elif str(n)[-1] == '3':
        return len('three')
    elif str(n)[-1] == '4':
        return len('four')
    elif str(n)[-1] == '5':
        return len('five')
    elif str(n)[-1] == '6':
        return len('six')
    elif str(n)[-1] == '7':
        return len('seven')
    elif str(n)[-1] == '8':
        return len('eight')
    elif str(n)[-1] == '9':
        return len('nine')


def check_ten_to_nineteen(n):
    if str(n)[-1] == '0':
        return len('ten')
    elif str(n)[-1] == '1':
        return len('eleven')
    elif str(n)[-1] == '2':
        return len('twelve')
    elif str(n)[-1] == '3':
        return len('thirteen')
    elif str(n)[-1] == '4':
        return len('fourteen')
    elif str(n)[-1] == '5':
        return len('fifteen')
    elif str(n)[-1] == '6':
        return len('sixteen')
    elif str(n)[-1] == '7':
        return len('seventeen')
    elif str(n)[-1] == '8':
        return len('eighteen')
    elif str(n)[-1] == '9':
        return len('nineteen')


def check_tens(n):
    if str(n)[-2] == '0':
        return 0 + check_digit(n)
    elif str(n)[-2] == '1':
        return check_ten_to_nineteen(n)
    elif str(n)[-2] == '2':
        return 6 + check_digit(n)
    elif str(n)[-2] == '3':
        return 6 + check_digit(n)
    elif str(n)[-2] == '4':
        return 5 + check_digit(n)
    elif str(n)[-2] == '5':
        return 5 + check_digit(n)
    elif str(n)[-2] == '6':
        return 5 + check_digit(n)
    elif str(n)[-2] == '7':
        return 7 + check_digit(n)
    elif str(n)[-2] == '8':
        return 6 + check_digit(n)
    elif str(n)[-2] == '9':
        return 6 + check_digit(n)


def check_hundreds(n):
    if str(n)[-2] == '0' and str(n)[-1] == '0':
        and_letters = 0
    else:
        and_letters = 3
    hundred = len('hundred')
    if str(n)[-3] == '1':
        return 3 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '2':
        return 3 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '3':
        return 5 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '4':
        return 4 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '5':
        return 4 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '6':
        return 3 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '7':
        return 5 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '8':
        return 5 + hundred + and_letters + check_tens(n)
    elif str(n)[-3] == '9':
        return 4 + hundred + and_letters + check_tens(n)


def main():
    letter_count = 0
    for x in range(1, 1001):
        print(x)
        if len(str(x)) == 1:
            letter_count += check_digit(x)
        if len(str(x)) == 2:
            letter_count += check_tens(x)
        if len(str(x)) == 3:
            letter_count += check_hundreds(x)
        if len(str(x)) == 4:
            letter_count += 11
    print(letter_count)


if __name__ == '__main__':
    main()
