"""
Code by Gonzalo Rolon Morinelli, Dec 24 2015.

The following code was originally written as a solution for Project Euler's
Problem# 17
For more information, goto: https://projecteuler.net/problem=17
"""


UNITS_DICT = {'0': 0,
              '1': 3,
              '2': 3,
              '3': 5,
              '4': 4,
              '5': 4,
              '6': 3,
              '7': 5,
              '8': 5,
              '9': 4}

TEN_DICT = {'10': 3,
            '11': 6,
            '12': 6,
            '13': 8,
            '14': 8,
            '15': 7,
            '16': 7,
            '17': 9,
            '18': 8,
            '19': 8}

TENS_DICT = {'0': 0,
             '2': 6,
             '3': 6,
             '4': 5,
             '5': 5,
             '6': 5,
             '7': 7,
             '8': 6,
             '9': 6}


def rc_num_letter_count(n):
    """Return the count of letters in the word representation of n <= 1000."""
    len_n = len(n)
    if len_n == 1:
        return UNITS_DICT[n]
    elif len_n == 4:
        return 11
    else:
        if len_n == 3:
            extra = 10 if n[1:] != '00' else 7
            return UNITS_DICT[n[0]] + extra + rc_num_letter_count(n[1:])
        if len_n == 2:
            if n[0] == '1':
                return TEN_DICT[n]
            else:
                return TENS_DICT[n[0]] + rc_num_letter_count(n[1])


def compute_sum_num_letter_lte(n):
    """Return the sum of letters in [1, n <= 1000].

    Returns the sum of letters used in the word representation of each
    number in [1, n<= 1000].
    """
    sum_letter = 0
    for num in range(1, n + 1):
        sum_letter += rc_num_letter_count(str(num))
    return sum_letter

if __name__ == '__main__':
    # Problem solution.
    print compute_sum_num_letter_lte(1000)
