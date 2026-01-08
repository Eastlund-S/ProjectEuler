"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


"""

from itertools import permutations

def main():
    perms = permutations(range(10))
    for index, iteration in enumerate(perms, start=1):
        if index == 1000000:
            answer = ""
            for digit in iteration:
                answer = answer + str(digit)
    print(answer)

    # perms = set()
    # for permutation in range(987654321):
        # string = str(permutation).zfill(10)
        # if len(set(string)) == len(string):
            # perms.add(string)
            # if len(perms) == 1000000:
                # print(string)


if __name__ == '__main__':
    main()
