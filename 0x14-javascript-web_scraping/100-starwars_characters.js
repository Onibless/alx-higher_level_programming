#!/usr/bin/node
const request = require('request');
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  JSON.parse(body).characters.forEach((item) => {
    const req = require('request');
    const personUrl = `${item}`;
    req.get(personUrl, (err, response, body) => {
      if (err) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
