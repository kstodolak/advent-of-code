#!/usr/bin/python3
import os
from collections import defaultdict

def get_hash(word):
  current = 0
  for c in word:
    current += ord(c)
    current *= 17
    current = current % 256
  
  return current

with open(os.path.dirname(__file__) + '/input.txt') as f:
  records = f.read().split(',')
  boxes = defaultdict(lambda: [])

  part1 = 0
  for word in records:
    part1 += get_hash(word)
  print(part1)

  # part 2
  for word in records:
    if '=' in word:
      label, focal_length = word.split('=')
      label_hash = get_hash(label)
      
      found = None
      for i,x in enumerate(boxes[label_hash]):
        if x[0] == label: 
          found = i
      if found is None: boxes[label_hash].append((label, int(focal_length)))
      else: boxes[label_hash][found] = (label, int(focal_length))
    elif '-' in word:
      label = word.split('-')[0]
      label_hash = get_hash(label)
      boxes[label_hash] = list(filter(lambda x: x[0] != label, boxes[label_hash]))
    else:
      assert False

  part2 = 0
  for i in range(256):
    box = boxes[i]
    for slot, (label, focal_length) in enumerate(box, start=1):
      to_add = (i+1) * slot * focal_length
      part2 += to_add
  
  print(part2)

