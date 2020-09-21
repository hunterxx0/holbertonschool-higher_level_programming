#!/usr/bin/node
const o_dict = require('./101-data').dict;
console.log(o_dict);
const n_dict = {}
for ( let key in o_dict) {
  if (n_dict[o_dict[key]] === undefined) {
    n_dict[o_dict[key]] = [key]
  }
  else {
    n_dict[o_dict[key]].push(key)
  }
}
console.log(n_dict);
