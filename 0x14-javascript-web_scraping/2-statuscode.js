#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];

if (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
} else {
  console.log('Missing URL');
}
