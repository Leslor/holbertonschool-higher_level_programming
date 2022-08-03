#!/usr/bin/node

const SquareBase = require('./5-rectangle');

module.exports = class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
