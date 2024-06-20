#!/usr/bin/node
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  charPrint (c) {
    let raw = '';
    if (c === undefined) {
      c = 'x';
    }
    for (let i = 0; i < this.width; i++) {
      raw = raw + c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(raw);
    }
  }
}

module.exports = Square;
