#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log('0');
} else {
  let result = [];
  for (let i = 2; i < len; i++) {
    result.unshift(process.argv[i]);
  }
  result = result.sort().reverse();
  console.log(result[1]);
}
