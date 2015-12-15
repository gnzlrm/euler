/**
Code by Gonzalo Rolon Morinelli, Dec 13 2015.

The following code was originally written as a solution for Project Euler's
Problem# 7
For more information, goto: https://projecteuler.net/problem=7
*/

function findNthPrime(n) {
    /*
    Return the nth prime.

    Modification to the Eratosthenes sieve using upper bound prime
    approximation for n >= 6.
    **/
    var counter = 0;
    var number = 2;
    var compSet = new Set();
    var lastPrime = null;
    var upper = n * Math.log(n) + n * Math.log(Math.log(n));
    while (counter < n) {
        if (!compSet.has(number)) {
            lastPrime = number;
            mult = Math.pow(lastPrime, 2);
            while (mult <= upper) {
                compSet.add(mult);
                mult += lastPrime;
            }
            counter += 1;
        }
        number += 1;
    }
    return lastPrime;
}

module.exports.findNthPrime = findNthPrime;

if (require.main === module) {
    console.log(findNthPrime(10001));
}
