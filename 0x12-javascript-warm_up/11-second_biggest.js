#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(1);
} else {
  let max = process.argv[2];
  let sm = 0;
  for (let i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      sm = max;
      max = process.argv[i];
    }
  }
  console.log(sm);
}
