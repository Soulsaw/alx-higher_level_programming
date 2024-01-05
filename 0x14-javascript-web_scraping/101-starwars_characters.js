#!/usr/bin/node
const request = require('request');
const userId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${userId}`;
request(url, { json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = body.characters;
    for (const idx in characters) {
      request(characters[idx], { json: true }, function (err, resp, bod) {
        if (!err && resp.statusCode === 200) {
          console.log(bod.name);
        }
      });
    }
  }
});
