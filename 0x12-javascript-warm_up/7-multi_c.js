#!/usr/bin/node
/*
script that prints 7 times C is fun
*/
const argument = process.argv;
const num = argument[2];
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
