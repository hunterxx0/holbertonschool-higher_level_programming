#!/usr/bin/node
const dict = require('./101-data').dict;
console.log(dict);
const ndict = {};
for (const key in dict) {
  if (ndict[dict[key]] === undefined) {
    ndict[dict[key]] = [key];
  } else {
    ndict[dict[key]].push(key);
  }
}
console.log(ndict);
