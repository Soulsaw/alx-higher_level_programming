#!/usr/bin/node
const firstArg = Number(process.argv[2]);
function factoriel (a) {
  if (isNaN(a) || a === 0 || a === 1) {
    return (1);
  } else {
    return (a * factoriel(a - 1));
  }
}
const fact = factoriel(firstArg);
console.log(fact);
