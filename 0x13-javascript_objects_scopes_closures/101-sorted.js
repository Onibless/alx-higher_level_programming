#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  // if (dict.hasOwnProperty.call(dict, key)) {

  console.log(key + ': ' + dict[key]);
  // }
}
