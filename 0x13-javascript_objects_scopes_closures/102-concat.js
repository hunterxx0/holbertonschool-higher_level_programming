#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], function (err1, data1) {
  fs.readFile(args[1], function (err2, data2) {
    let data = data1 + '\n' + data2 + '\n';
    fs.writeFile(args[2], data, { flag: 'wx' }, function (err) {
      if (err) throw err;
    });
  });
});



/*
fs.readFile(args[0], function (err1, data1) {
  fs.readFile(args[1], function (err2, data2) {
    if (err1 || err2) {
      throw new Error();
    }
    const data = data1 + data2;
    fs.writeFile(args[2], data);
  });
});
*/
