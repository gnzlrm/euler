"""
Code by Gonzalo Rolon Morinelli, Sep 10 2015.

The following code was originally written as a solution for Project Euler's
Problem# 5
For more information, goto: https://projecteuler.net/problem=5
"""


import p003_primes as primes_import


def find_lcm_lt(n):
    """Return the Least Common Multiple of all numbers in range [2, n)."""
    primes = primes_import.get_primes_lt(n)
    max_powers = set(primes)
    for prime in primes:
        prime_power = prime ** 2
        if prime_power < n:
            while prime_power * prime < n:
                prime_power *= prime
            max_powers.remove(prime)
            max_powers.add(prime_power)
    return reduce(lambda x, y: x * y, max_powers)

if __name__ == '__main__':
    # Problem solution
    print find_lcm_lt(20)
