/**
Code by Gonzalo Rolon Morinelli, Dec 12 2015.

The following code was originally written as a solution for Project Euler's
Problem# 3
For more information, goto: https://projecteuler.net/problem=3
*/

function getPrimesLt(n) {
    /**
    Return a list with all the prime numbers lesser than n.

    Custom implementation of Eratosthenes's sieve.
    */
    var compSet = new Set();
    var primeList = [];
    var number = 2;
    while (number < n) {
        if (!compSet.has(number)) {
            primeList.push(number);
            var multiple = number * number;
            while (multiple < n) {
                compSet.add(multiple);
                multiple += number;
            }
        }
        number += 1;
    }
    return primeList;
}

function getLargestPrimeFactor(n) {
    /**
    Return the largest prime factor of the input composite number n.

    If n is unusual, it returns the second largest prime factor instead.
    */
    var primes = getPrimesLt(Math.sqrt(n) + 1);
    primes.reverse();
    for (var prime of primes) {
        if (n % prime === 0) {
            return prime;
        }
    }
    return -1;
}

module.exports.getPrimesLt = getPrimesLt;
module.exports.getLargestPrimeFactor = getLargestPrimeFactor;

if (require.main === module) {
    // Problem solution
    console.log(getLargestPrimeFactor(600851475143));
}
