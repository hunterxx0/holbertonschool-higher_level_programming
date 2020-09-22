#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const result = {}
request(args[0], function (error, response, body) {
  res = JSON.parse(body);
  for (x in res) {
    if (res[x].completed == true) {
      if (result[res[x].userId] === undefined) {
	result[res[x].userId] = 1;
      } else {
	result[res[x].userId] = result[res[x].userId] + 1;
      }
    }
  }
  console.log(result);
});
