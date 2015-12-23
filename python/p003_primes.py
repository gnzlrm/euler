"""
Code by Gonzalo Rolon Morinelli, Sep 9 2015.

The following code was originally written as a solution for Project Euler's
Problem# 3
For more information, goto: https://projecteuler.net/problem=3
"""


import math


def get_primes_lt(n):
    """Return a list with all the prime numbers lesser than n.

    Custom implementation of Eratosthenes's sieve.
    """
    comp_set = set([])
    prime_list = []
    number = 2
    while number < n:
        if number not in comp_set:
            prime_list.append(number)
            multiple = number * number
            while multiple < n:
                comp_set.add(multiple)
                multiple += number
        number += 1
    return prime_list


def find_largest_prime_factor(n):
    """Return the largest prime factor of the input composite number n.

    If n is unusual, it returns the second largest prime factor instead.
    """
    primes = get_primes_lt(math.sqrt(n) + 1)
    primes.reverse()
    for prime in primes:
        if n % prime == 0:
            return prime
    return -1


if __name__ == '__main__':
    # Problem solution
    print find_largest_prime_factor(600851475143)
