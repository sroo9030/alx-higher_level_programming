#!/usr/bin/node

const process = require('process');
const args = process.argv;

const num = parseInt(args[2]);

function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (!isNaN(num)) {
  const fac = factorial(num);
  console.log(fac);
} else {
  console.log('1');
}
