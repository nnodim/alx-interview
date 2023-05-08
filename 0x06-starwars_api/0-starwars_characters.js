#!/usr/bin/node
const request = require("request");

const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

function makeRequest(characters, index) {
  if (characters.length === index) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      makeRequest(characters, index + 1);
    }
  });
}

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data["characters"];

    makeRequest(characters, 0);
  }
});
