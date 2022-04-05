#!/usr/bin/node
const myValue = 'C is fun';
const args = process.argv[2];
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args; i++) { console.log(myValue); }
}
