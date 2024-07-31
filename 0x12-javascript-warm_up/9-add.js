#!/usr/bin/node

const process = require('process');
const args = process.argv;

const num1 = Math.floor(parseFloat(args[2]));
const num2 = Math.floor(parseFloat(args[3]));

function add (a, b) {
  const result = a + b;
  return result;
}

if (!isNaN(num1) && !isNaN(num2)) {
  const sum = add(num1, num2);
  console.log(sum);
} else {
  console.log('NaN');
}
