#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = {};
  list.forEach(function (x) { count[x] = (count[x] || 0) + 1; });
  return count[searchElement];
};
