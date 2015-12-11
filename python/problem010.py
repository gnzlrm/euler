"""Code by Gonzalo Rolon Morinelli, Sep 21 2015.

The following code was originally written as a solution for Project Euler's
Problem# 10.
For more information, goto: https://projecteuler.net/problem=10
"""

import problem003

if __name__ == '__main__':
    # Problem solution
    print sum(problem003.get_primes_lt(2000000))
