#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log(data);
});
