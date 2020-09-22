#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
request(args[0], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(args[1], body, { flag: 'wx' }, function (err) {
    if (err) throw err;
  });
});
