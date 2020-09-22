#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0];
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const result = {};
  const res = JSON.parse(body).characters;
  for (let x = 0; x < res.length; x++) {
    request(res[x], function (error1, response1, body1) {
      if (error) {
        return console.log(error);
      }
      result[x] = JSON.parse(body1).name;
      if (x === res.length - 1) {
        for (let z = 0; z < res.length; z++) {
          console.log(result[z]);
        }
      }
    });
  }
});
