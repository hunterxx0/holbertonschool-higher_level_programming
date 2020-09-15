#!/usr/bin/node
function fac (x) {
  if (x === 0) {
    return 1;
  }
  return x * fac(x - 1);
}
if (process.argv[2] === undefined || isNaN(Number(process.argv[2]))) {
  console.log(fac(0));
} else {
  console.log(fac(parseInt(process.argv[2])));
}
