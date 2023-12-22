#!/usr/bin/python3
import os
import math
from copy import deepcopy

workflows = dict()

letters = {
  'x': 0,
  'm': 1,
  'a': 2,
  's': 3,
}

def solve_part2():
  start = ('in', [[1, 4000], [1, 4000], [1, 4000], [1, 4000]])
  todo = [start]

  result = 0
  while todo:
    curr = todo.pop(0)
    key, ranges = curr

    if not all(b-a>0 for a,b in ranges): continue
    if key == 'R': continue

    if key == 'A':
      score = math.prod(b-a+1 for a,b in ranges)
      result += score
      continue

    for r in workflows[key]:
      if r.isalnum():
        todo.append((r, ranges))
        break
      condition, target = r.split(':')
      new_ranges = deepcopy(ranges)
      if '<' in condition:
        a, b = condition.split('<')
        b = int(b)
        letter = letters[a]
        if b-1 < new_ranges[letter][1]:
          new_ranges[letter][1] = b-1
        if b > ranges[letter][0]:
          ranges[letter][0] = b
      elif '>' in condition:
        a, b = condition.split('>')
        b = int(b)
        letter = letters[a]
        if b+1 > new_ranges[letter][0]:
          new_ranges[letter][0] = b+1
        if b < ranges[letter][1]:
          ranges[letter][1] = b

      todo.append((target, new_ranges))
  
  return result


with open(os.path.dirname(__file__) + "/input.txt") as f:
  lines = f.read().splitlines()
  parts = []

  while lines:
    curr = lines.pop(0)
    if curr == "":
      break
    name, rest = curr.split("{") 
    rest = rest.replace("}", "")
    rest = rest.split(",")
    workflows[name] = rest


  print(solve_part2())
 