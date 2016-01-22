/**
Code by Gonzalo Rolon Morinelli, Jan 22 2016.

The following code was originally written as a solution for Project Euler's
Problem# 15
For more information, goto: https://projecteuler.net/problem=15
*/


function factorial(n) {
    // Return the product of all positive integers <= n.
    if (n <= 1) {
        return 1;
    }
    return factorial(n - 1) * n;
}


function computeLatticePaths(idx, jdx) {
    // Return the amount of Lattice paths from origin to (idx, jdx).
    return factorial(idx + jdx) / (factorial(jdx) * factorial(idx));
}


module.exports.factorial = factorial;
module.exports.computeLatticePaths = computeLatticePaths;

if (require.main === module) {
    console.log(computeLatticePaths(20, 20));
}
