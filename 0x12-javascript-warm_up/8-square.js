#!/usr/bin/node
const args = process.argv.slice(2);
const size = Number(args[0]);
let raw = '';
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    raw = raw + 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(raw);
  }
} else {
  console.log('Missing size');
}
