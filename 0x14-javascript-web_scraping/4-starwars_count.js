#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
count = 0;
request(args[0], function (error, response, body) {
  res = JSON.parse(body).results;
  for (x in res) {
    for (charac in res[x].characters) {
      if (res[x].characters[charac].slice(37, -1) == '18') {
	count++;
      }
    }
  }
  console.log(count);
});
