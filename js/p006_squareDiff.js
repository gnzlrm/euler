/**
Code by Gonzalo Rolon Morinelli, Dec 13 2015.

The following code was originally written as a solution for Project Euler's
Problem# 6
For more information, goto: https://projecteuler.net/problem=6
*/

function getSumSquaresLt(n) {
    // Return the sum of the squares of all numbers in interval (0, n].
    return (n * (n + 1) * (2 * n + 1)) / 6;
}

function getSquaresSumLt(n) {
    // Return the square of the sum of all numbers in interval (0, n].
    interval = [];
    for (i = 0; i < n + 1; i++) {
        interval.push(i);
    }
    return Math.pow(interval.reduce((a, b) => a + b), 2);
}

module.exports.getSumSquaresLt = getSumSquaresLt;
module.exports.getSumSquaresLt = getSquaresSumLt;

if (require.main === module) {
    // Problem solution.
    console.log(getSquaresSumLt(100) - getSumSquaresLt(100));
}
