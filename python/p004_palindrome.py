"""
Code by Gonzalo Rolon Morinelli, Sep 9 2015.

The following code was originally written as a solution for Project Euler's
Problem# 4
For more information, goto: https://projecteuler.net/problem=4
"""


def get_all_palindromes_digits(n):
    """Return all the possible palindromic numbers of input length n."""
    if n == 1:
        return set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    else:
        prev_palindrome = get_all_palindromes_digits(n - 1)
        palindromes = set([])
        for pal_num in prev_palindrome:
            for i in range(0, 10):
                num_str = str(pal_num)[:n / 2] + str(i) + str(pal_num)[n / 2:]
                if num_str == num_str[::-1]:
                    palindromes.add(int(num_str))
        return palindromes


def find_largest_palindrome_multiple(n):
    """Find the largest palindromic multiple.

    Returns a tuple containing the largest palindromic number multiple of
    two numbers of input length n, and it's two factors.
    """
    start_idx = (10 ** n) - 1
    end_idx = (start_idx / 10)
    palindromes = list(get_all_palindromes_digits(n * 2))
    palindromes.sort(reverse=True)
    for pal_num in palindromes:
        for idx in range(start_idx, end_idx, -1):
            if pal_num % idx == 0 and end_idx < pal_num / idx <= start_idx:
                return (pal_num, idx, pal_num / idx)

if __name__ == '__main__':
    # Problem solution
    print find_largest_palindrome_multiple(3)
