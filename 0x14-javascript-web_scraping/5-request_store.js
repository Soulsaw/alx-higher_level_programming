#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request(url, { html: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(path, body, 'utf-8', (error) => {
      if (error) {
        process.exit(1);
      }
    });
  }
});
