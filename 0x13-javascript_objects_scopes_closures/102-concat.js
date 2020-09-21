#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
let data = '';
fs.readFile(args[0], 'utf8', function (err1, data1) {
  fs.readFile(args[1], 'utf8', function (err2, data2) {
    if (err1 || err2) {
      return console.log(err1 || err2);
    }
    data = data1 + data2;
    fs.writeFile(args[2], data, { flag: 'wx' }, function (err) {
      if (err) throw err;
    });
  });
});
