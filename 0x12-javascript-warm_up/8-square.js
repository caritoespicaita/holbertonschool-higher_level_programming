#!/usr/bin/node
const args = process.argv[2];
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let j = 0; j < args; j++) {
    console.log('X'.repeat(args));
  }
}
