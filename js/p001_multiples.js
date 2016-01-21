/**
Code by Gonzalo Rolon Morinelli, Dec 11 2015.

The following code was originally written as a solution for Project Euler's
Problem# 1
For more information, goto: https://projecteuler.net/problem=1
*/

/*jshint esnext: true*/

function sumMultiples (multipliers, limit) {
    // Return the sum of all multiples of [multipliers] < the input limit.
    var multiplesSum = 0;
    for (i = 0; i < limit; i++) {
        for (var multiple of multipliers) {
            if (i % multiple === 0) {
                multiplesSum += i;
                break;
            }
        }
    }
    return multiplesSum;
}

module.exports.sumMultiples = sumMultiples;

if (require.main === module) {
    // Problem solution
    console.log(sumMultiples([3, 5], 1000));
}
