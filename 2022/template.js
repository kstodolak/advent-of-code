(require('../utils/arrayUtils'))();
const fs = require('fs');
const path = require('path');

function main(input) {
  return input;
}

fs.readFile(path.resolve(__dirname, 'input.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return;
  }

});
