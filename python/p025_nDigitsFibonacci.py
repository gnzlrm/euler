"""
Code by Gonzalo Rolon Morinelli, Jan 5 2016.

The following code was originally written as a solution for Project Euler's
Problem# 25
For more information, goto: https://projecteuler.net/problem=25
"""


from math import log10

PHI = (5 ** 0.5 + 1) / 2


def find_n_digit_fibonacci(n):
    """Return the term of the first fibonacci number that has n digits.

    Combines closed-form formula to approximate the n-th fibonacci number with
    the standard digit calculation (log10 + 1).
    """
    idx = round((log10(10) * (n - 1) + log10(5) / 2) / log10(PHI))
    return int(idx)

if __name__ == '__main__':
    # Problem solution.
    print find_n_digit_fibonacci(1000)
