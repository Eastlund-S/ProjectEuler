"""
n! means n x(n -1) ×⋯ x3 x2 x1.

For example, 10! =10 x9 ×⋯ x3 x2 x1 =3628800,
and the sum of the digits in the number 10! is 3 +6 +2 +8 +8 +0 +0 =27.

Find the sum of the digits in the number 100!.

648
"""

def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number
    return result

def main():
    n = 100
    print(f"Factorial of {n} is {factorial(n)}")
    digits = str(factorial(n))
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)
    print(f"Sum of digits of factorial is {sum_of_digits}")

if __name__ == '__main__':
    main()
