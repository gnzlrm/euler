"""
Code by Gonzalo Rolon Morinelli, Dec 31 2015.

The following code was originally written as a solution for Project Euler's
Problem# 21
For more information, goto: https://projecteuler.net/problem=21
"""


from math import sqrt


def get_sum_divisors(n):
    """Get the sum of all the divisors of n."""
    divs = 1
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            divs += num + (n / num)
    return divs


def compute_amicable_lt(n):
    """Get all amicable numbers < n."""
    amicable = set([])
    non_amicable = set([])
    for num in range(2, n):
        if num not in non_amicable and num not in amicable:
            div_sum = get_sum_divisors(num)
            if get_sum_divisors(div_sum) == num and num != div_sum:
                amicable.add(num)
                amicable.add(div_sum)
            else:
                non_amicable.add(div_sum)
    return amicable


if __name__ == '__main__':
    # Problem solution.
    print sum(compute_amicable_lt(10000))
