/**
Code by Gonzalo Rolon Morinelli, Dec 15 2015.

The following code was originally written as a solution for Project Euler's
Problem# 8
For more information, goto: https://projecteuler.net/problem=8
*/

function findGreatestProduct(n, tNum) {
    /**
    Find greatest product of consecutive numbers.

    Find the greatest product of the sequence of n consecutive numbers
    in the input tNum.
    */
    var tSeqs = [];
    var zeroIdx = tNum.split('').reduce(function(a, v, i) {
        if (v === '0') {
            a.push(i);
        }
        return a;
    }, [-1]);
    zeroIdx.push(tNum.length);
    var zeroDist = zeroIdx.reduce(function(a, v, i, p) {
        if (i < p.length - 1) {
            a.push(p[i + 1] - v);
        }
        return a;
    }, []);
    for (i = 0; i < zeroDist.length; i++) {
        if (zeroDist[i] >= n) {
            var initIdx = zeroIdx[i] + 1;
            var endIdx = initIdx + n;
            while (endIdx <= zeroIdx[i + 1]) {
                tSeqs.push(tNum.slice(initIdx, endIdx));
                initIdx += 1;
                endIdx += 1;
            }
        }
    }
    var maxMul = 0;
    for (var seq of tSeqs) {
        var seqMul = seq.split('').reduce(function(a, b) { return a * b; });
        if (seqMul > maxMul) {
            maxMul = seqMul;
        }
    }
    return maxMul;
}

module.exports.findGreatestProduct = findGreatestProduct;

if (require.main === module) {
    // Problem solution.
    console.log(findGreatestProduct(13, '73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747152386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'));
}
