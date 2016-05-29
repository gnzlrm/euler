"""
Code by Gonzalo Rolon Morinelli, Jan 1 2016.

The following code was originally written as a solution for Project Euler's
Problem# 22
For more information, goto: https://projecteuler.net/problem=22
"""


import os
import re


def read_list_file(path):
    """Return a sorted list of strings with the file content given it's path.

    Make a list of letter-only strings with the file content splitting by
    commas.
    """
    with open(path, 'r') as tgt_file:
        list_string = map(lambda x: re.sub(r'\W+', '', x), tgt_file.read().split(','))
        list_string.sort()
        return list_string


def get_name_score(name, idx):
    """Return the name score of a given name and index in a sorted namelist.

    Name score is determine by the sum of the ordinal rank of each
    letter of name in respect to the alphabet times the ordinal rank of name
    in a sorted namelist.
    """
    return sum(map(lambda x: ord(x) - 64, name)) * (idx + 1)  # - 64 for upper.


def compute_total_name_score(path):
    """Compute the total name score of all names in a file located at path."""
    namelist = read_list_file(path)
    score = 0
    for idx, name in enumerate(namelist):
        score += get_name_score(name, idx)
    return score


if __name__ == '__main__':
    # Problem solution.
    print compute_total_name_score(os.getcwd() + "/p022_names.txt")
