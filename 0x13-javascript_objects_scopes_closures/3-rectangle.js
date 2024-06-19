#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let raw = '';
    for (let i = 0; i < this.width; i++) {
      raw = raw + 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(raw);
    }
  }
}

module.exports = Rectangle;
