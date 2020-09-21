#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list1 = list.map(x => (x * Number(list.indexOf(x))));
console.log(list1)
