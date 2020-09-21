#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let tmp = c;
      for (let j = 0; j < this.width - 1; j++) {
        tmp += c;
      }
      console.log(tmp);
    }
  }
};
