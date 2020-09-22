#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
count = 0;
url = 'https://swapi-api.hbtn.io/api/films/' + args[0];
request(url, function (error, response, body) {
  res = JSON.parse(body).characters;
  for (x in res) {
    request(res[x], function (error1, response1, body1) {
      console.log(JSON.parse(body1).name);
    });
  }
});
