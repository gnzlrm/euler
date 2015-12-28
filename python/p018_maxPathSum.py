"""
Code by Gonzalo Rolon Morinelli, Dec 24 2015.

The following code was originally written as a solution for Project Euler's
Problem# 18
For more information, goto: https://projecteuler.net/problem=18
"""


from p011_largestProdGrid import parse_num_multistring


def compute_max_path(tri_list, idx):
    """Compute the maximum sum in the paths in triangle tri_list."""
    i_one = idx + 1
    if len(tri_list) == 1:
        return max(tri_list[0][idx], tri_list[0][i_one])
    else:
        return max(tri_list[0][idx] + compute_max_path(tri_list[1:], idx),
                   tri_list[0][i_one] + compute_max_path(tri_list[1:], i_one))


if __name__ == '__main__':
    # Problem solution.
    tri_list = parse_num_multistring("""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""")
    print tri_list[0][0] + compute_max_path(tri_list[1:], 0)
