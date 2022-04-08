#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; list[i]; i++) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }
  return (count);
};
