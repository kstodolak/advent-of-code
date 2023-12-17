#!/usr/bin/python3
import os
import sys
from queue import PriorityQueue
from collections import defaultdict

DIRECTIONS = [
  (-1,0), # 0 - N - Up
  (1,0),  # 1 - S - Down
  (0,-1), # 2 - W - Left
  (0,1)   # 3 - E - Right
]

def is_reversed(dir_i, dir_ii):
  if dir_i is None or dir_ii is None: return False
  if dir_i == dir_ii: return False
  (y, x) = DIRECTIONS[dir_i]
  (yy, xx) = DIRECTIONS[dir_ii]
  if y != 0 and yy != 0: return y != yy
  if x != 0 and xx != 0: return x != xx

  return False

def cheapest_path(G, start=(0,0), part1=True):
  pq = PriorityQueue()
  pq.put((0, start, None, -1)) # dist, pos/vertex, direction, how_long_in_direction

  visited = set()

  result = sys.maxsize # shortest distance to end
  while not pq.empty():
    (dist, pos, dir_i, dir_count) = pq.get()
    if (pos, dir_i, dir_count) in visited: continue
    visited.add((pos, dir_i, dir_count))

    (y,x) = pos
    if y == len(G)-1 and x == len(G[0])-1:
      result = min(result, dist)
      continue

    for new_dir_i, (dy, dx) in enumerate(DIRECTIONS):
      yy = y + dy
      xx = x + dx
      if yy not in range(len(G)) or xx not in range(len(G[0])): continue
      if is_reversed(dir_i, new_dir_i): continue
      new_dir_count = 1 if new_dir_i != dir_i else dir_count + 1
      
      if part1 and new_dir_count > 3: continue
      if not part1:
        if new_dir_count > 10: continue
        if new_dir_i != dir_i and dir_count < 4 and dir_count != -1: continue

      cost = G[yy][xx]
      pq.put((dist+cost, (yy, xx), new_dir_i, new_dir_count))

  return result

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  G = [[int(l) for l in line] for line in lines]
  height = len(G)
  width = len(G[0])

  print(cheapest_path((G), (0,0), True))
  print(cheapest_path((G), (0,0), False))

