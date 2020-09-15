#!/usr/bin/node
function add (a, b) {
  return a + b;
}
if (process.argv[2] !== undefined && process.argv[3] !== undefined &&
  !isNaN(Number(process.argv[2])) && !isNaN(Number(process.argv[3]))) {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
} else {
  console.log(NaN);
}
