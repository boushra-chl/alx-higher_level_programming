#!/usr/bin/node
const args = process.argv.slice(2);
let n = Number(args[0]);
if (!isNaN(n)) {
  console.log(`My number: ${n}`);
} else {
  console.log('Not a number');
}
