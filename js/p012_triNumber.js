/**
Code by Gonzalo Rolon Morinelli, Jan 20 2016.

The following code was originally written as a solution for Project Euler's
Problem# 12
For more information, goto: https://projecteuler.net/problem=12
*/

/*jshint esnext: true*/

var extend = require('util')._extend;

function getPrimeFactors(n) {
    // Return a dict with the prime factorization of n.
    var primeDict = {};
    for (num = 2; num < Math.sqrt(n) + 1; num++) {
        while (n % num === 0) {
            primeDict[num] = (primeDict[num] || (primeDict[num] = 0)) + 1;
            n /= num;
        }
    }
    if (n > 1) {
        primeDict[n] = 1;
    }
    return primeDict;
}

function getTrinumDivisors(nFactor, mFactor) {
    // Return the |divisors| of n * m / 2, given their prime factorization.
    var tFactor = extend(nFactor, mFactor);
    tFactor[2] -= 1;
    if (tFactor[2] === null) {
        delete tFactor[2];
    }
    var pows_one = Object.keys(tFactor).map(key => tFactor[key] + 1);
    return pows_one.reduce((a, b) => a * b);
}

function computeTrinumDivisorsGt(x) {
    // Return the first triangle number with > x divisors.
    var n = 1;
    var m = 2;
    var mFactor = {2: 1};
    var divisors = 1;
    while (divisors <= x) {
        n = m;
        m += 1;
        nFactor = mFactor;
        mFactor = getPrimeFactors(m);
        divisors = getTrinumDivisors(nFactor, mFactor);
    }
    return n * m / 2;
}

module.exports.getPrimeFactors = getPrimeFactors;
module.exports.getTrinumDivisors = getTrinumDivisors;
module.exports.computeTrinumDivisorsGt = computeTrinumDivisorsGt;

if (require.main === module) {
    // Problem solution.
    console.log(computeTrinumDivisorsGt(500));
}
