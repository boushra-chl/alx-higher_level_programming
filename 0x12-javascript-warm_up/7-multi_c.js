#!/usr/bin/node
args = process.argv.slice(2);
const x = Number(args[0]);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
else {
  console.log('Missing number of occurrences');
}
