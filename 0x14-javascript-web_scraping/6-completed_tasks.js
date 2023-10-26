#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const info = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.forEach((item) => {
      if (item.completed) {
        const userId = item.userId;
        if (!info[userId]) {
          info[userId] = 1;
        } else {
          info[userId] += 1;
        }
      }
    });
    console.log(info);
  }
});
