"""
Code by Gonzalo Rolon Morinelli, Dec 27 2015.

The following code was originally written as a solution for Project Euler's
Problem# 20
For more information, goto: https://projecteuler.net/problem=20
"""


from math import factorial


if __name__ == '__main__':
    # Problem solution.
    print reduce(lambda x, y: int(x) + int(y), str(factorial(100)))
