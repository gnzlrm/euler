"""
Code by Gonzalo Rolon Morinelli, Dec 24 2015.

The following code was originally written as a solution for Project Euler's
Problem# 15
For more information, goto: https://projecteuler.net/problem=15
"""


from math import factorial


def compute_lattice_paths(idx, jdx):
    """Return the amount of Lattice paths from origin to (idx, jdx)."""
    return factorial(idx + jdx) / (factorial(jdx) * factorial(idx))


if __name__ == '__main__':
    # Problem solution.
    print compute_lattice_paths(20, 20)
