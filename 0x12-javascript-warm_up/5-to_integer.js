#!/usr/bin/node
/*
prints the first argument converted to an integer
*/
const argument = process.argv;
const num = Number(argument[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  const result = 'My number: ' + num;
  console.log(result);
}
