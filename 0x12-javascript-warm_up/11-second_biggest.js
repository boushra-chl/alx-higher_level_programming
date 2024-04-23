#!/usr/bin/node
/*
prints second biggest integer in the list of arguments
*/
const argument = process.argv;
const len = process.argv.length;
if (argument[2] === undefined) {
  console.log('0');
} else if (len === 3) {
  console.log('0');
} else {
  let max = argument[2];
  let secondMax = argument[2];
  for (let i = 2; i < len; i++) {
    if (argument[i] > max) {
      max = argument[i];
    }
  }
  for (let i = 2; i < len; i++) {
    if (argument[i] < max && argument[i] >= secondMax) {
      secondMax = argument[i];
    }
  }
  console.log(secondMax);
}
