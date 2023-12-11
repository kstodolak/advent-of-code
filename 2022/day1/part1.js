(require('../utils/arrayUtils'))();
const fs = require('fs');
const path = require('path');


function getMaxDeerCalories(caloriesInput) {
  const calories = []

  let actualCalories = 0
  caloriesInput.forEach(el => {
    if (el === '') {
      calories.push(actualCalories);
      actualCalories = 0;
      return;
    }

    actualCalories += Number(el);
  });

  return calories.max();
}

fs.readFile(path.resolve(__dirname, 'input.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const dataSplitted = data.trim().split('\n');
  const result = getMaxDeerCalories(dataSplitted);
  console.log(result);
});
