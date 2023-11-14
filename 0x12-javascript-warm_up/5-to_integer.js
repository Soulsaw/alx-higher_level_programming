#!/usr/bin/node
const myNumber = Number(process.argv[2]);
if (process.argv[2] !== undefined) {
  if (isNaN(myNumber)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${myNumber}`);
  }
}
