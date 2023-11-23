#!/usr/bin/node
const myNumber = Number(process.argv[2]);
if (isNaN(myNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNumber; i++) {
    console.log('X'.repeat(myNumber));
  }
}
