#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  let max = 0;
  let sm = 0;
  if (parseInt(process.argv[2]) > parseInt(process.argv[3])) {
    max = parseInt(process.argv[2]);
    sm = parseInt(process.argv[3]);
  } else {
    max = parseInt(process.argv[3]);
    sm = parseInt(process.argv[2]);
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      sm = max;
      max = process.argv[i];
    }
  }
  console.log(sm);
}
