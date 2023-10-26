#!/usr/bin/node

const request = require('request');
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const dataArray = [];

function printArry (ar) {
  for (let i = 0; i < ar.length; i++) {
    console.log(ar[i]);
  }
}

request.get(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const promises = [];

  characters.forEach((item) => {
    const personUrl = item;
    const promise = new Promise((resolve, reject) => {
      request.get(personUrl, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    promises.push(promise);
  });

  Promise.all(promises)
    .then((names) => {
      dataArray.push(...names);
      printArry(dataArray);
    })
    .catch((err) => {
      console.log(err);
    });
});
