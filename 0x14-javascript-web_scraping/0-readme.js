#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.slice(0, -1));
});
