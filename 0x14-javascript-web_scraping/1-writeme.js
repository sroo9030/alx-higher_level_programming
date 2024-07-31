#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

if (filePath && stringToWrite) {
  fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
} 
