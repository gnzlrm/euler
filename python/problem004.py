"""Code by Gonzalo Rolon Morinelli, Sep 9 2015.

The following code was originally written as a solution for Project Euler's
Problem# 4
For more information, goto: https://projecteuler.net/problem=4
"""


def get_all_palindromes_digits(length):
    """Return all the possible palindromic numbers of input length."""
    if length == 1:
        return set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    else:
        prev_palindrome = get_all_palindromes_digits(length - 1)
        palindromes = set([])
        for palindrome in prev_palindrome:
            for idx in range(0, 10):
                number_string = str(palindrome)[:length / 2]
                + str(idx) + str(palindrome)[length / 2:]
                if number_string == number_string[::-1]:
                    palindromes.add(int(number_string))
        return palindromes


def find_largest_palindrome_multiple(length):
    """Find the largest palindromic multiple.

    Returns a tuple containing the largest palindromic number multiple of
    two numbers of input length, and it's two factors.
    """
    start_idx = (10 ** length) - 1
    end_idx = (start_idx / 10)
    palindromes = list(get_all_palindromes_digits(length * 2))
    palindromes.sort(reverse=True)
    for pal_num in palindromes:
        for idx in range(start_idx, end_idx, -1):
            if pal_num % idx == 0 and end_idx < pal_num / idx <= start_idx:
                return (pal_num, idx, pal_num / idx)

if __name__ == '__main__':
    # Problem solution
    print find_largest_palindrome_multiple(3)
