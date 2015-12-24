"""
Code by Gonzalo Rolon Morinelli, Dec 24 2015.

The following code was originally written as a solution for Project Euler's
Problem# 16
For more information, goto: https://projecteuler.net/problem=16
"""


def get_power_digit_sum(n, pow):
    """Return the sum of the digits of n ** pow."""
    return reduce(lambda x, y: int(x) + int(y), str(n ** pow))


if __name__ == '__main__':
    # Problem solution.
    print get_power_digit_sum(2, 1000)
