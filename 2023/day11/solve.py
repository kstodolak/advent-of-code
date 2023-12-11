#!/usr/bin/python3
import os
# import numpy as np

def expand_map(M):
  new_M = []
  for x in range(len(M)):
    if all(M[yy][x] == '.' for yy in range(len(M))):
      for y in range(len(M[0])):
        M[y].insert(x,'o')
  
def find_empty_rows(M):
  result = []
  for y in range(len(M)):
    empty = True
    for x in range(len(M[y])):
      if M[y][x] == '#': 
        empty = False
        break
    if empty: result.append(y)
  
  return result

def find_empty_cols(M):
  result = []
  for x in range(len(M[0])):
    empty = True
    for y in range(len(M)):
      if M[y][x] == '#': 
        empty = False
        break
    if empty: result.append(x)
  
  return result


with open(os.path.dirname(__file__) + '/input.txt') as f:
  M = f.read().splitlines()
  for i,line in enumerate(M):
    M[i] = [c for c in line]

  galactics = []
  for y in range(len(M)):
    for x in range(len(M[y])):
      if M[y][x] == '#':
        galactics.append((y,x))

  empty_rows = find_empty_rows(M)
  empty_columns = find_empty_cols(M)

  multiplier = 1
  multiplier2 = 1000000-1 
  part1 = 0
  part2 = 0
  for i,(y,x) in enumerate(galactics):
    for (yy,xx) in galactics[i:]:
      min_x = min(x,xx)
      min_y = min(y,yy)
      max_x = max(x,xx)
      max_y = max(y,yy)
      dis = abs(yy-y)+abs(xx-x)
      dis2 = abs(yy-y)+abs(xx-x)
      for row in empty_rows:
        if min_y <= row  and row <= max_y:
          dis += multiplier
          dis2 += multiplier2
      
      for col in empty_columns:
        if min_x <= col and col <= max_x:
          dis += multiplier
          dis2 += multiplier2
      part1 += dis
      part2 += dis2

  print(part1)
  print(part2)