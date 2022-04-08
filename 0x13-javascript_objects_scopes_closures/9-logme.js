#!/usr/bin/node
const list = [];
exports.logMe = function (item){
let idx = list.indexOf(item);
list.push(item);
idx = list.indexOf(item, idx + 1);
console.log(idx + ":" + list[idx]);
};