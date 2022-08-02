#!/usr/bin/node
if (parseInt(process.argv.length) <= 3) {
  console.log(0);
} else {
  let i, max1, max2;
  max1 = parseInt(process.argv[2]);
  max2 = max1;
  for (i = 3; i < parseInt(process.argv.length); i++) {
    if (parseInt(process.argv[i]) > max1) {
      max2 = max1;
      max1 = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > max2) {
      max2 = parseInt(process.argv[i]);
    }
  }
  console.log(max2);
}
