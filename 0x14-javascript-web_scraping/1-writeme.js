#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(args[0], args[1], { flag: 'wx' }, function (err) {
  if (err) throw err;
});
