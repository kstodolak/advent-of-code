(require('../utils/arrayUtils'))();
const fs = require('fs');
const path = require('path');

fs.readFile(path.resolve(__dirname, 'input.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return;
  }

  const result = round2(data.trim().split('\n'));
  console.log(result);
});


function round2(input) {
  const groups = [];
  while (input.length) {
    groups.push([
      input.shift(),
      input.shift(),
      input.shift(),
    ]);
  }

  const duplicates = groups.map(getLinesDuplicates);

  return duplicates.flat().map(el => {
    if (el.toUpperCase() === el) {
      return el.charCodeAt(0) - 38;
    }
    return el.charCodeAt(0) - 96;
  }).sum();
}


function getLinesDuplicates(input) {
  const substrings = [];

  const toCompare = input[0].split('');
  toCompare.forEach(el => {
    if (input[1].includes(el) && input[2].includes(el)) substrings.push(el);
  });

  return substrings.uniq();
}
