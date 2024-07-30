#!/usr/bin/node

const process = require('process');
const args = process.argv;
let count = 0;

args.forEach((val, index) => {
  count++;
  if (count === 3) {
    console.log(`${val}`);
  }
});

if (count !== 3) {
  console.log('No argument');
}
