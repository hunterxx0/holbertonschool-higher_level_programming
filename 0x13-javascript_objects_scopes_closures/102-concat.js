#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
let data = ''
fs.readFile(args[0], 'utf8', function (err,data1) {
  fs.readFile(args[1], 'utf8', function (err,data2) {
    if (err) {
      return console.log(err);
    }
    data = data1 + data2;
    fs.writeFile(args[2], data, { flag: 'wx' }, function (err) {
      if (err) throw err;
    });
  });
});
