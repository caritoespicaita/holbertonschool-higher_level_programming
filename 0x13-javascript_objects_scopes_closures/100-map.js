#!/usr/bin/node
const list = require('./100-data.js').list;

const map1 = list.map((num, index) => {
  return num * index;
});
console.log(list);
console.log(map1);
