#!/usr/bin/node
/*
script that computes factorial of an integer
*/
const argument = process.argv;
const num = Number(argument[2]);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(num));
