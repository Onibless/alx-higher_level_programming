#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const title = JSON.parse(body).title;
    console.log(title);
  }
});
