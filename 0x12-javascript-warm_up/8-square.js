#!/usr/bin/node
/*
prints a square
*/
const argument = process.argv;
const num = Number(argument[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
