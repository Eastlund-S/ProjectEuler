"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every
route. However, Problem 67, is the same challenge with a triangle containing
one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

answer = 1313 Not correct! I can't just rearrange the triangle how I want to!
answer = 1074

"""

import numpy as np

TRIANGLE = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def split_on_lines(string):
    split_string = []
    for line in string.splitlines():
        line = line.strip().split(' ')
        if not line:
            continue
        split_string.append(line)
    return split_string


# I made this and then realised I couldn't just change the triangle
# when I want to!
def bubble_sort(array):
    # print(x[0])
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True


def main():
    triangle = split_on_lines(TRIANGLE)
    for x in range(len(triangle)):
        for y in range(len(triangle[x])):
            triangle[x][y] = int(triangle[x][y])
    left_val = 0
    right_val = 0
    for x in reversed(range(len(triangle) - 1)):
        step_values = []
        for n in range(len(triangle) - 1):
            try:
                left_val = triangle[x][n] + triangle[x+1][n]
                right_val = triangle[x][n] + triangle[x+1][n+1]
            except IndexError:
                pass
            if left_val > right_val:
                step_values.append(left_val)
            else:
                step_values.append(right_val)
        triangle[x] = step_values
    largest_route_val = triangle[0][0]
    print(largest_route_val)


if __name__ == '__main__':
    main()
