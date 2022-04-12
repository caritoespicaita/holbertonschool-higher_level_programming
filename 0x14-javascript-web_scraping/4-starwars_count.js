#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const id = '/18/'

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body).results;
  let count = 0;
  for (let movie of json){
      for (let findCharcter of movie.characters){
          if (findCharcter.endsWith(id)){count ++}
      }
  }
  console.log(count);  
});