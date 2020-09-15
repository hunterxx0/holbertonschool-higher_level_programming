#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  const arr = process.argv.slice();
  arr.shift();
  arr.shift();
  console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
}
