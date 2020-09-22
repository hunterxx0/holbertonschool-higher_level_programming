#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request(args[0], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
