"""
Code by Gonzalo Rolon Morinelli, Jan 2 2016.

The following code was originally written as a solution for Project Euler's
Problem# 23
For more information, goto: https://projecteuler.net/problem=23
"""


from p021_amicableNumbers import get_sum_divisors


def get_abundants_sum_lt(n):
    """Return all numbers that are the sum of two abundant numbers < n."""
    abundants = []
    abundants_sum = set([])
    for num in range(12, n):
            if get_sum_divisors(num) > num:
                abundants.append(num)
                for abundant in abundants:
                    if abundant + num >= n:
                        break
                    else:
                        abundants_sum.add(abundant + num)
    return abundants_sum


def compute_sum_non_abundants_sum_lt(n):
    """Return the sum of all numbers that aren't the sum of two abundants."""
    abundants_sum = get_abundants_sum_lt(n)
    non_abundants_sum = 0
    for number in range(n):
        if number not in abundants_sum:
            non_abundants_sum += number
    return non_abundants_sum


if __name__ == '__main__':
    # Problem solution.
    print compute_sum_non_abundants_sum_lt(28123)
