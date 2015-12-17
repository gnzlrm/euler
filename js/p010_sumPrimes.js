/**
Code by Gonzalo Rolon Morinelli, Dec 16 2015.

The following code was originally written as a solution for Project Euler's
Problem# 10
For more information, goto: https://projecteuler.net/problem=10
*/

var primesImport = require('./p003_primes.js');

if (require.main === module) {
    // Problem solution.
    console.log(primesImport.getPrimesLt(2000000).reduce(function(a, b) {
        return a + b;
    }));
}
