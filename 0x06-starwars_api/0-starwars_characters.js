#!/usr/bin/node
const request = require("request");

const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make request for movie data
request(movieUrl, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const data = JSON.parse(body);
    const characters = data["characters"];

    // Loop through characters and print each one
    characters.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode == 200) {
          const characterData = JSON.parse(body);
          console.log(characterData["name"]);
        }
      });
    });
  }
});
