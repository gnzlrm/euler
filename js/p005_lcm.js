/**
Code by Gonzalo Rolon Morinelli, Dec 12 2015.

The following code was originally written as a solution for Project Euler's
Problem# 5
For more information, goto: https://projecteuler.net/problem=5
*/

var primesImport = require('./p003_primes.js');

function findLcmLt(n) {
    // Return the Least Common Multiple of all numbers in range [2, n).
    var primes = primesImport.getPrimesLt(n);
    maxPowers = new Set(primes);
    for (var prime of primes) {
        var primePower = Math.pow(prime, 2);
        if (primePower < n) {
            while (primePower * prime < n) {
                primePower *= prime;
            }
            maxPowers.delete(prime);
            maxPowers.add(primePower);
        }
    }
    return Array.from(maxPowers).reduce((a, b) => a * b);
}

module.exports.findLcmLt = findLcmLt;

if (require.main === module) {
    // Problem solution
    console.log(findLcmLt(20));
}
