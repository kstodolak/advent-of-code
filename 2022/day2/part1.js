(require('../utils/arrayUtils'))();
const fs = require('fs');
const path = require('path');

fs.readFile(path.resolve(__dirname, 'input.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return;
  }

  const rounds = data.trim().split('\n');
  let myResult = 0;
  rounds.forEach(round => {
    const [opponent, me] = round.split(' ');

    if (opponent === 'A') {
      if (me === 'X') {
        myResult = myResult + 3 + 1;
        return;
      }
      if (me === 'Y') {
        myResult = myResult + 6 + 2;
        return;
      }
      if (me === 'Z') {
        myResult = myResult + 0 + 3;
        return;
      }
    }
    if (opponent === 'B') {
      if (me === 'X') {
        myResult = myResult + 0 + 1;
        return;
      }
      if (me === 'Y') {
        myResult = myResult + 3 + 2;
        return;
      }
      if (me === 'Z') {
        myResult = myResult + 6 + 3;
        return;
      }

    }
    if (opponent === 'C') {
      if (me === 'X') {
        myResult = myResult + 6 + 1;
        return;
      }
      if (me === 'Y') {
        myResult = myResult + 0 + 2;
        return;
      }
      if (me === 'Z') {
        myResult = myResult + 3 + 3;
        return;
      }
    }
  });

  console.log(myResult);
});
