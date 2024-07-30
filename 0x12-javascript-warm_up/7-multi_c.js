#!/usr/bin/node

const process = require('process');
const args = process.argv;

const num = Math.floor(parseFloat(args[2]));

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
