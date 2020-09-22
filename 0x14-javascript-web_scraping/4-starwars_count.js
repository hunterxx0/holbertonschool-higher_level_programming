#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
let count = 0;
request(args[0], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const res = JSON.parse(body).results;
  for (const x in res) {
    for (const charac in res[x].characters) {
      if (res[x].characters[charac].slice(37, -1) === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
