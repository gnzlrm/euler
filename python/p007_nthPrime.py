"""
Code by Gonzalo Rolon Morinelli, Sep 13 2015.

The following code was originally written as a solution for Project Euler's
Problem# 7
For more information, goto: https://projecteuler.net/problem=7
"""

import math


def find_nth_prime(n):
    """
    Return the nth prime.

    Modification to the Eratosthenes sieve using upper bound prime
    approximation for n >= 6.
    """
    counter = 0
    number = 2
    comp_set = set([])
    last_prime = None
    upper = n * math.log(n) + n * math.log(math.log(n))
    while counter < n:
        if number not in comp_set:
            last_prime = number
            mult = last_prime ** 2
            while mult <= upper:
                comp_set.add(mult)
                mult += last_prime
            counter += 1
        number += 1
    return last_prime

if __name__ == '__main__':
    # Problem solution
    print find_nth_prime(10001)
