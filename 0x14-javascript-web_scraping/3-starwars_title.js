#!/usr/bin/node

const request = require('request');
const process = require('process');
const args = process.argv;

if (args.length < 3) {
  console.log('Please provide a movie ID');
  process.exit(1);
}

const movieId = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (res.statusCode === 200) {
    console.log(body.title);
  } else {
    console.log('Movie not found');
  }
});
