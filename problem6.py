# Code by Gonzalo Rolon Morinelli, Sep 12 2015
# The following code was originally written as a solution for Project Euler's Problem# 6
# For more information, goto: https://projecteuler.net/problem=6

def get_sum_squares_lt(n):
    """
    Return the sum of the squares of all numbers in interval (0, n]
    """
    return (n * (n + 1) * (2 * n + 1)) / 6

def get_square_sum_lt(n):
    """
    Return the square of the sum of all numbers in interval (0, n]
    """
    interval = range(n + 1)
    return sum(interval) ** 2

if __name__ == '__main__':
    print get_square_sum_lt(100) - get_sum_squares_lt(100)
