#!/usr/bin/python3
import os, re
from collections import defaultdict

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  part1=0
  part2=0
  card_counter=defaultdict(lambda: 1)
  card_counter[0] = 1
  for i, line in enumerate(lines, start=1):
    (p1, p2) = line.split('|')
    i, *winning = list(map(int,re.findall(r'(\d+)', p1)))
    mine = list(map(int,re.findall(r'\d+', p2)))

    multiplier=1 # 1 | 2 | 4 | 8 ..
    round_score = 0
    matches=0 # part 2
    for number in mine:
      if number in winning:
        round_score = multiplier
        multiplier *= 2
        matches += 1
    
    for ii in range(matches):
      card_counter[i+ii+1] += card_counter[i]

    part2 += card_counter[i]
    part1 += round_score

  print(part1)
  print(part2) # 9881048
  