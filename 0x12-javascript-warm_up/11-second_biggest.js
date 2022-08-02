#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  const max2 = Math.max.apply(null, arr);
  console.log(max2);
}
