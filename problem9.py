# Code by Gonzalo Rolon Morinelli, Sep 20 2015
# The following code was originally written as a solution for Project Euler's Problem# 9
# For more information, goto: https://projecteuler.net/problem=9

def find_pyth_triplet(sum_t):
    """
    Return the Plato's Pythagorean triplet (a, b, c)
    for which a + b + c = sum_t, if any.
    Return a = b = c = -1 if not.
    """
    non_mul_flag = True
    m = 2
    a = b = c = None
    while non_mul_flag:
        a, b, c = (2 * m), (m ** 2 - 1), (m ** 2 + 1)
        t = a + b + c
        if sum_t % t == 0:
            non_mul_flag = False
        elif t > sum_t:
            return (-1, -1, -1)
        else:
            m += 1
    return (a * sum_t / t, b * sum_t / t, c * sum_t / t)

if __name__ == '__main__':
    # Problem solution
    print reduce(lambda x, y: x * y, find_pyth_triplet(1000))
