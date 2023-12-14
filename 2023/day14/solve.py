#!/usr/bin/python3
import os
from copy import deepcopy

CYCLES = 1000000000 # 1 000 000 000

def move_rock(D, y, x):
  yy = y 
  move_to = y
  while yy > 0:
    yy -= 1
    c = D[yy][x]
    if c == '.':
      move_to = yy
    else:
      break
  
  if move_to != y:
    D[move_to][x] = 'O'
    D[y][x] = '.'

def part1(D):
  DD = deepcopy(D)
  for y in range(1,len(D)):
    for x in range(len(D[y])):
      if D[y][x] == 'O': 
        move_rock(DD, y, x)

  print(count_load(DD))

def rotate(D):
  return [
    [x for x in row]
    for row in list(zip(*D[::-1]))
  ]

def run_cycle(D):
  for _ in range(4):
    for y in range(1, len(D)):
      for x in range(len(D[y])):
        if D[y][x] == 'O':
          move_rock(D, y, x)

    D = rotate(D)
  return D
    
def count_load(D):
  h = len(D)
  result = 0
  for y in range(h):
    for x in range(len(D[y])):
      if D[y][x] == 'O': result += h - y

  return result

def hash_list(D):
  as_str = ""
  for y in range(len(D)):
    for x in range(len(D[y])):
      as_str += D[y][x]
  
  return hash(as_str)

with open(os.path.dirname(__file__) + '/input.txt') as f:
  D = []
  lines = f.read().splitlines()

  for line in lines:
    row = [l for l in line]
    D.append(row)

  part1(D) # 113456

  hashes = [hash_list(D)]
  cycle_to = cycle_len = None
  for i in range(CYCLES):
    D = run_cycle(D)
    new_hash = hash_list(D)
    if new_hash in hashes: # found cycle
      cycle_to = i + 1
      cycle_len = cycle_to - hashes.index(new_hash)
      break

    hashes.append(new_hash)
  
  iterations_left = CYCLES - cycle_to

  for i in range(iterations_left % cycle_len):
    D = run_cycle(D)
  
  print(count_load(D))

