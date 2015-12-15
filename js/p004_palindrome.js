/**
Code by Gonzalo Rolon Morinelli, Dec 11 2015.

The following code was originally written as a solution for Project Euler's
Problem# 4
For more information, goto: https://projecteuler.net/problem=4
*/

function getAllPalindromesDigits(n) {
    // Return all the possible palindromic numbers of input length n.
    if (n === 1) {
        return new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    } else {
        var prevPalindrome = getAllPalindromesDigits(n - 1);
        var palindromes = new Set();
        for (var palNum of prevPalindrome) {
            for (i = 0; i < 10; i++) {
                var numStr = palNum.toString().slice(0, n / 2) + i.toString() + palNum.toString().slice(n / 2);
                if (numStr == numStr.split('').reverse().join('')) {
                    palindromes.add(parseInt(numStr));
                }
            }
        }
        return palindromes;
    }
}

function findLargestPalindromeMultiple(n) {
    /**
    Find the largest palindromic multiple.

    Returns a tuple containing the largest palindromic multiple of
    two numbers of input length n, and it's two factors.
    */
    var startIdx = Math.pow(10, n) - 1;
    var endIdx = (startIdx / 10);
    var palindromes = Array.from(getAllPalindromesDigits(n * 2));
    palindromes.sort(function(a, b) {return b - a;});
    for (var palNum of palindromes) {
        for (i = startIdx; i > endIdx; i--) {
            if ((palNum % i === 0) && (endIdx < palNum / i) && (palNum / i <= startIdx)) {
                return [palNum, i, palNum / i];
            }
        }
    }
}

module.exports.getAllPalindromesDigits = getAllPalindromesDigits;
module.exports.findLargestPalindromeMultiple = findLargestPalindromeMultiple;

if (require.main === module){
    // Problem solution.
    console.log(findLargestPalindromeMultiple(3));
}
