#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (list === undefined) {
    return 0;
  }
  const count = {};
  list.forEach(function (x) { count[x] = (count[x] || 0) + 1; });
  if (count[searchElement] === undefined) {
    return 0;
  }
  return count[searchElement];
};
