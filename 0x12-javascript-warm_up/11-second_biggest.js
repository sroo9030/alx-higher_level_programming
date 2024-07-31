#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg)).sort((a, b) => b - a);
  console.log(nums[1]);
}
