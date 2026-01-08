"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	=0.5
1/3	=0.(3)
1/4	=0.25
1/5	=0.2
1/6	=0.1(6)
1/7	=0.(142857)
1/8	=0.125
1/9	=0.(1)
1/10	=0.1
 
Where 0.1(6) means 0.166666⋯, and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d <1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""

def long_division(dividend, divisor):
    """dividend / divisor"""



def main():
    """Find the longest recurring decimal
    - """
    # Source - https://stackoverflow.com/a/79414145
    # Posted by Peter4075
    # Retrieved 2025-12-23, License - CC BY-SA 4.0

    repeating_decimal_periods = []
    repeating_decimal_denominators = []

    for d in range(1, 1000): # d is the denominator
        for n in range (1, 1000):
            if (10**n)%d == 1:
                repeating_decimal_periods.append(n) 
                repeating_decimal_denominators.append(d)
                break

    max_period = max(repeating_decimal_periods)
    x = repeating_decimal_periods.index(max_period)
    denominator = repeating_decimal_denominators[x]
    print(max_period)
    print(denominator)

def old():
    """This doesn't work because the numbers are too long."""
    for x in range(1, 1000):
        print(f"Assessing {x}. It has a 1/x of {1/x}")
        result = str(1/x).split('.')[1] # Get's everything on the rhs of the decimal
        half_len = len(result) // 2
        # print(f"'{result}' is {len(result)} chars long. Half of it is {half_len}")
        for start in range(half_len):
            for length in range(1, half_len):
                # print(length)
                # print(result[start:(start + length)])
                # print(result[(start + length):(start + length + length)])
                if result[start:(start + length)] == result[(start + length):(start + length + length)]:
                    recurring = result[start:(start + length)]
                    print(f"The string {recurring} is {length} long. It belongs to {x}")
                    break
            break
                    # if length > 7:
                        # print(f"{x} gives a {result} returning a maximum length of {length}")
                        # # print(result[start:length])

if __name__ == '__main__':
    main()
