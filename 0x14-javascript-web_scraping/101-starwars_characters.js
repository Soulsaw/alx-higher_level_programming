#!/usr/bin/node
const request = require('request');
const userId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${userId}`;
request(url, { json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const charactersPromises = body.characters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, { json: true }, function (err, resp, bod) {
          if (!err && resp.statusCode === 200) {
            resolve(bod.name);
          } else {
            reject(err);
          }
        });
      });
    });
    Promise.all(charactersPromises)
      .then(characterName => console.log(characterName.join('\n')))
      .catch(characterErr => console.log(characterErr));
  }
});
