#!/usr/bin/node
const entry = require('./100-data').list;

console.log(entry);

const newList = entry.map((x, index) => x * index);
console.log(newList);
