#!/usr/bin/node
const fs = require('fs');

const path = process.argv[2];
const cotnent = process.argv[3];

fs.appendFile(path, cotnent, (error) => {
  if (error) {
    console.log(error);
  }
});
