#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0];
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const res = JSON.parse(body).characters;
  for (const x in res) {
    request(res[x], function (error1, response1, body1) {
      if (error1) {
        return console.log(error1);
      }
      console.log(JSON.parse(body1).name);
    });
  }
});
