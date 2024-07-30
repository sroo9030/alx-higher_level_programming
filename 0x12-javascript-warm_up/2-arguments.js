#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length === 3) {
  console.log('Argument found');
} else if (args.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
