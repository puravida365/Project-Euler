/* Multiples of 3 and 5

url: https://projecteuler.net/problem=1

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. */

var max_value = 1000;
var multiples = [];

for (var i = 0; i < max_value; i++ ){
    if ((i % 3 == 0) || (i % 5 == 0)){
        multiples.push(i);
    }
}

sum = multiples.reduce(function (a, b) {return a + b;}, 0);

document.write(sum);

/* Result

233168

*/