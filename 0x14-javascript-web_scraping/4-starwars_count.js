#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '18';
let i = 0;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(id)) {
          i++;
        }
      });
    });
    console.log(i);
  }
});
