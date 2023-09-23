#!/usr/bin/node

const list = require('./100-data.js').list;
// console.log(list.map((x) => list.indexOf(x) * x));
console.log(list);
console.log(list.map((value, index) => value * index));
