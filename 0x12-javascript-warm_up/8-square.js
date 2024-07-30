#!/usr/bin/node

const process = require('process');
const args = process.argv;

const num = Math.floor(parseFloat(args[2]));

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('x'.repeat(num));
  }
} else {
  console.log('Missing size');
}
