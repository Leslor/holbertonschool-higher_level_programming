#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (i of list) {
    if (i == searchElement) {
      counter++;
    }
  }
};
