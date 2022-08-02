#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let i, max1, max2;
  max1 = process.argv[2];
  max2 = max1;
  for (i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > max1) {
      max2 = max1;
      max1 = process.argv[i];
    } else if (process.argv[i] > max2) {
      max2 = process.argv[i];
    }
  }
  console.log(max2);
}
