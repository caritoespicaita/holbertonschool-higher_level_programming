#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const id = '/18/';

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body).results;
  let count = 0;
  for (const movie of json) {
    for (const findCharcter of movie.characters) {
      if (findCharcter.endsWith(id)) { count++; }
    }
  }
  console.log(count);
});
