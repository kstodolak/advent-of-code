#!/usr/bin/python3
import os, re

digits_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  part1 = 0
  for line in lines:
    digits = re.findall(r'\d', line)
    if len(digits) == 0: continue
    assert int(digits[0]+digits[-1]) < 100
    part1 += int(digits[0]+digits[-1])
  

  # part 2
  part2 = 0
  for line in lines:
    digits = []
    for i,c in enumerate(line):
      if c.isdigit():
        digits.append(c)
        continue

      for ii,word in enumerate(digits_as_words, start=1):
        if line[i:].startswith(word):
          digits.append(str(ii))

    part2 += int(digits[0]+digits[-1])
    
  print(part1)
  print(part2)