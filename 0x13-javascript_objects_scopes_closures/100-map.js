#!/usr/bin/node
const list = require('./100-data.js').list;

const map1 = list.map((num) => num * list.indexOf(num));

console.log(list);
console.log(map1);
