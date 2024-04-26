#!/usr/bin/node
const SquareP = require('./5-square.js');
class Square extends SquareP {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        if (typeof c === 'undefined') {
          row = row + 'X';
        } else {
          row = row + c;
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
