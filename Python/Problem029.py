"""
9183
"""


def problem_29():
    terms = {a**b for a in range(2,101) for b in range(2,101)}
    print(len(sorted(terms)))


if __name__ == '__main__':
    problem_29()
