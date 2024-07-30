#!/usr/bin/node

const process = require('process');
const args = process.argv;

const num = Math.floor(parseFloat(args[2]));

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
