#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = process.argv[2];
  const X = 'X'.repeat(x);
  for (let i = 0; i < x; i++) {
    console.log(X);
  }
}
