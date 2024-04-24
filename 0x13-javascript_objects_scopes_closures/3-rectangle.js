#!/usr/bin/node
class Rectangle {
  constructor (h, w) {
    if (h <= 0 || w <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row = row + 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
