#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];

if (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
} else {
  console.log('Missing file path');
}
