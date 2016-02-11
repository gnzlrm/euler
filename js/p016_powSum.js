/**
Code by Gonzalo Rolon Morinelli, Feb 11 2016.

The following code was originally written as a solution for Project Euler's
Problem# 16
For more information, goto: https://projecteuler.net/problem=16
*/

var BigNumber = require('big-number').n;

function getPowerDigitSum(n, pow) {
    // Return the sum of the digits of n ** pow.
    res = BigNumber(n).power(pow).toString();
    return res.split('').reduce((x, y) => parseInt(x) + parseInt(y));
}

if (require.main === module) {
    console.log(getPowerDigitSum(2, 1000));
}
