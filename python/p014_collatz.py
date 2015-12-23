"""
Code by Gonzalo Rolon Morinelli, Dec 21 2015.

The following code was originally written as a solution for Project Euler's
Problem# 14
For more information, goto: https://projecteuler.net/problem=14
"""


def rcmem_collatz_ln(n, k_lens={1: 0}):
    """Return the length of the Collatz sequence yield by n."""
    if n in k_lens:
        return k_lens[n]
    else:
        k_lens[n] = rcmem_collatz_ln(3 * n + 1 if n % 2 else n / 2) + 1
        return k_lens[n]


def compute_longest_collatz(n):
    """Return the number < n that yields the longest Collatz sequence."""
    max_len = float('-inf')
    for num in range(1, n):
        c_len = rcmem_collatz_ln(num)
        if c_len > max_len:
            max_len = c_len
            max_num = num
    return max_num

if __name__ == '__main__':
    print compute_longest_collatz(1000000)
