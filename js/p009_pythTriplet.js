/**
Code by Gonzalo Rolon Morinelli, Dec 16 2015.

The following code was originally written as a solution for Project Euler's
Problem# 9
For more information, goto: https://projecteuler.net/problem=9
*/

/*jshint esnext: true*/

function findPythTriplet(sumT) {
    /**
    Return Pythagorean triplet for which a + b + c = sum_t.

    Return the Plato's Pythagorean triplet (a, b, c)
    for which a + b + c = sum_t, if any.
    Return a = b = c = -1 if not.
    */
    var nonMulFlag = true;
    var m = 2;
    var a = b = c = t = null;
    while (nonMulFlag === true) {
        a = 2 * m;
        b = Math.pow(m, 2) - 1;
        c = Math.pow(m, 2) + 1;
        t = a + b + c;
        if (sumT % t === 0) {
            nonMulFlag =  false;
        } else if (t > sumT) {
            return [-1];
        } else {
            m += 1;
        }
    }
    return ([(a * (sumT / t)), (b * (sumT / t)), (c * (sumT / t))]);
}

module.exports.findPythTriplet = findPythTriplet;

if (require.main === module) {
    // Problem solution.
    console.log(findPythTriplet(1000).reduce((a, b) => a * b));
}
