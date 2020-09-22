#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request(args[0], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let count = 0;
  const res = JSON.parse(body).results;
  for (const x in res) {
    if (res[x].characters) {
      for (const charac in res[x].characters) {
        if (res[x].characters[charac] &&
            res[x].characters[charac] ===
            'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
  }
  console.log(count);
});
