"""
Code by Gonzalo Rolon Morinelli, Sep 8 2015.

The following code was originally written as a solution for Project Euler's
Problem# 1
For more information, goto: https://projecteuler.net/problem=1
"""


def sum_multiples(multipliers, limit):
    """Return the sum of all multiples of [multipliers] < the input limit."""
    multiples_sum = 0
    for idx in range(limit):
        for multiplier in multipliers:
            if idx % multiplier == 0:
                multiples_sum += idx
                break
    return multiples_sum

if __name__ == '__main__':
    # Problem solution
    print sum_multiples([3, 5], 1000)
