const fs = require('fs');
const path = require('path');


fs.readFile(path.resolve(__dirname, 'input2.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return;
  }

  const pairs = data.trim().split('\n');
  const paisMapped = pairs.map(el => el.split(','));

  const fullyDuplicated = 0;
  const partlyDuplicated = 0;
  paisMapped.forEach(([elf1, elf2]) => {
    const [elf1Start, elf1End] = elf1.split('-').map(el => parseInt(el, 10));
    const [elf2Start, elf2End] = elf2.split('-').map(el => parseInt(el, 10));

    if (elf2Start >= elf1Start && elf2End <= elf1End) {
      fullyDuplicated++;
      return
    }

    if (elf1Start >= elf2Start && elf1End <= elf2End) {
      fullyDuplicated++;
    }
  });

  paisMapped.forEach(([elf1, elf2]) => {
    const [elf1Start, elf1End] = elf1.split('-').map(el => parseInt(el, 10));
    const [elf2Start, elf2End] = elf2.split('-').map(el => parseInt(el, 10));

    if (elf1Start >= elf2Start && elf1Start <= elf2End) {
      partlyDuplicated++;
      return
    }

    if (elf2Start >= elf1Start && elf2Start <= elf1End) {
      partlyDuplicated++;
    }
  });

  console.log(fullyDuplicated);
  console.log(partlyDuplicated);
});
