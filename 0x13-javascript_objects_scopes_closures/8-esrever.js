#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length; i > 0; i--) {
    rev.push(list[i - 1]);
  }
  return (rev);
};
