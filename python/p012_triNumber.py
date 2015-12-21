"""
Code by Gonzalo Rolon Morinelli, Dec 20 2015.

The following code was originally written as a solution for Project Euler's
Problem# 12
For more information, goto: https://projecteuler.net/problem=12
"""


def get_prime_factors(n):
    """Return a dict with the prime factorization of n."""
    primeDict = {}
    for num in range(2, int(n ** 0.5 + 1)):
        while n % num == 0:
            primeDict[num] = primeDict.setdefault(num, 0) + 1
            n /= num
    if n > 1:
        primeDict[n] = 1
    return primeDict


def get_trinum_divisors(n_factor, m_factor):
    """Return the |divisors| of n * m / 2, given their prime factorization."""
    t_factor = dict(m_factor)
    for key in n_factor.keys():
        t_factor[key] = t_factor.setdefault(key, 0) + n_factor[key]
    t_factor[2] -= 1  # Reduce the powers of 2 by 1 to equal the division.
    if t_factor[2] == 0:
        del t_factor[2]
    pows_one = map(lambda x: x + 1, t_factor.values())
    return reduce(lambda x, y: x * y, pows_one)


def compute_trinumber_num_divisors(x):
    """Return the first triangle number with > x divisors."""
    n = 1
    m = 2
    m_factor = {2: 1}
    divisors = 1
    while divisors <= x:
        n = m
        m += 1
        n_factor = m_factor
        m_factor = get_prime_factors(m)
        divisors = get_trinum_divisors(n_factor, m_factor)
    return n * m / 2

if __name__ == '__main__':
    # Problem solution.
    print compute_trinumber_num_divisors(500)
