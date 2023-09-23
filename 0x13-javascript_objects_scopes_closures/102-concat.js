#!/usr/bin/node

const fs = require('fs');

const firFile = process.argv[2];
const secFile = process.argv[3];
const thirFile = process.argv[4];

const readFirst = fs.readFileSync(firFile);
const readSec = fs.readFileSync(secFile);
fs.writeFileSync(thirFile, readFirst + readSec);
