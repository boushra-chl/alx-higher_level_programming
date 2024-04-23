#!/usr/bin/node
/*
adds 2 integers
*/
const argument = process.argv;
const num1 = Number(argument[2]);
const num2 = Number(argument[3]);
function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
