"""
Code by Gonzalo Rolon Morinelli, Jan 2 2016.

The following code was originally written as a solution for Project Euler's
Problem# 24
For more information, goto: https://projecteuler.net/problem=24
"""


from math import factorial, floor


def get_nth_permutation(elements, n):
    """Return the n-th lexicographical permutation of sorted elements."""
    if len(elements) == 1:
        return elements
    else:
        rem_fact = factorial(len(elements) - 1)
        idx = int(floor(n / rem_fact))
        rst = n - (idx * rem_fact)
        if rst == 0:
            idx -= 1
            rst = n - (idx * rem_fact)
        rem_str = elements[:idx] + elements[idx + 1:]
        return elements[idx] + get_nth_permutation(rem_str, rst)


if __name__ == '__main__':
    print get_nth_permutation('0123456789', 1000000)
