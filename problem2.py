# Code by Gonzalo Rolon Morinelli, Sep 8 2015
# The following code was originally written as a solution for Project Euler's Problem# 2
# For more information, goto: https://projecteuler.net/problem=1

def generate_fibonacci():
    """
    Return an unlimited Fibonacci's sequence generator.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    # Problem solution
    fib_generator = generate_fibonacci()
    sum_even = 0
    next_fib = fib_generator.next()
    while next_fib < 4000000:
        if next_fib % 2 == 0:
            sum_even += next_fib
        next_fib = fib_generator.next()
    print sum_even
