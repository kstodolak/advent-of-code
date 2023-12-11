(require('../utils/arrayUtils'))();
const fs = require('fs');
const path = require('path');


fs.readFile(path.resolve(__dirname, 'input.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const result1 = round1(data.split('\n'));
  console.log(result1);
});


function round1(input) {
  const substrings = [];
  input.forEach(round => {
    const roundResult = [];
    const part1 = round.slice(0, round.split('').midIndex()).split('');
    const part2 = round.slice(round.split('').midIndex());

    part1.forEach(p1 => {
      if (part2.includes(p1)) {
        roundResult.push(p1);
      }
    });

    substrings.push(roundResult.uniq());
  });

  return substrings.map(el => {
    return el.reduce((partSum, a) => {
      if (a.toUpperCase() === a) {
        return partSum += a.charCodeAt(0) - 38;
      }
      return partSum += a.charCodeAt(0) - 96;
    }, 0);
  }).sum()
}
