#!/usr/bin/node
function factorial (n) {
  const total = 1;
  if (!n) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));
