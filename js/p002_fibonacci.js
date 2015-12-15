/**
Code by Gonzalo Rolon Morinelli, Dec 12 2015.

The following code was originally written as a solution for Project Euler's
Problem# 2
For more information, goto: https://projecteuler.net/problem=2
*/

function* generateFibonacci () {
    // Return an unlimited Fibonacci's sequence generator.
    var a = 0;
    var b = 1;
    while (true) {
        var curr = a;
        yield a;
        a = b;
        b += curr;
    }
}

module.exports.generateFibonacci = generateFibonacci;

if (require.main === module) {
    // Problem solution
    fibGenerator = generateFibonacci();
    sumEven = 0;
    nextFib = fibGenerator.next().value;
    while (nextFib < 4000000) {
        if (nextFib % 2 === 0) {
            sumEven += nextFib;
        }
        nextFib = fibGenerator.next().value;
    }
    console.log(sumEven);
}
