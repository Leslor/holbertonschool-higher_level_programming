#!/usr/bin/node

let number = 0;
exports.logMe = function count (item) {
  console.log(`${number}: ${item}`);
  number += 1;
};
