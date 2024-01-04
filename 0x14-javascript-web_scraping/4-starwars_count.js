#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const resp = JSON.parse(body)
    const movieWithWedgeAntille = resp.results.filter((movie)=>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    )
    console.log(movieWithWedgeAntille.length);
  }
});
