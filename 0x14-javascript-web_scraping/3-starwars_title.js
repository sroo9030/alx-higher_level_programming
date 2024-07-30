#!/usr/bin/node

const request = require('request');
const process = require('process');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (movieId) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const film = JSON.parse(body);
      console.log(film.title);
    } else {
      console.log(`Error: ${response.statusCode}`);
    }
  });
} else {
  console.log('Missing movie ID');
}
