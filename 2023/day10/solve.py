#!/usr/bin/python3
import os

#   ( Y, X)
N = (-1, 0)
S = ( 1, 0)
E = ( 0, 1)
W = ( 0,-1)

# PIPES - (destinations, entrances_from)
PIPES = {
  '|': ((N,S), (S, N)), # can go North and South | can entrance from South and North
  '-': ((E,W), (W,E)),
  'L': ((N,E), (S, W)),
  'J': ((N,W), (S, E)),
  '7': ((S,W), (N, E)),
  'F': ((S,E), (N, W)),
  '.': ((), ()),
  'S': ((N,S,W,E), (N,S,W,E)),
}

def where_can_go(pipes, pos, prev):
  directions = PIPES[pipes[pos[0]][pos[1]]][0]
  for d in directions:
    calc_d = (pos[0] + d[0], pos[1] + d[1])
    if calc_d == prev: continue
    d_pipe = PIPES[pipes[calc_d[0]][calc_d[1]]][1]
    if d in d_pipe: 
      return calc_d
  return None

def get_neighbours(pos, visited):
  neighbours = []
  for (y,x) in [N,S,W,E]:
    new_pos = (pos[0] + y, pos[1] + x)
    if new_pos not in visited:
      neighbours.append()

def extend_map(M):
  new_M = []
  for y in range(len(M)):
    new_M.append(M[y])
    new_row = ['_' for _ in range(len(M[y]))]
    for x in range(len(M[y])):
      c = M[y][x]
      if c in ['S', 'F', '7', '|']:
        new_row[x] = '|'
    if new_row.count('_') != len(new_row):
      new_M.append(new_row)
  
  M = new_M
  for y in range(len(M)):
    new_row = []
    for x in range(len(M[y])-1):
      c = M[y][x]
      new_row.append(c)
      if c in ['S', '-', 'F', 'L']:
        new_row.append('-')
      else:
        new_row.append('_')
    M[y] = new_row

  return M

def flood(M):
  start = (0,0)
  todo = [start]
  visited = set(start)
  while len(todo) > 0:
    (y,x) = todo.pop(0)
    if M[y][x] == '.': M[y][x] = 'o'
    for (yy,xx) in [N,S,W,E]:
      (new_y, new_x) = (y + yy, x + xx)
      if (new_y, new_x) not in visited:
        if new_y in range(len(M)) and new_x in range(len(M[0])):
          if M[new_y][new_x] in ['.', '_']:
            visited.add((new_y, new_x))
            todo.append((new_y, new_x))

  return M


def traverse(pipes, start, M):
  steps = 0
  pos = start
  prev = None

  while True:
    next_pos = where_can_go(pipes, pos, prev)
    assert next_pos is not None
    prev = pos
    pos = next_pos
    M[pos[0]][pos[1]] = pipes[pos[0]][pos[1]]
    steps += 1
    if pos == start and steps != 0: break

  print(steps//2)

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  M = [['.' for ll in l] for l in lines]
  start = None
  for y,l in enumerate(lines):
    if l.find('S') > -1:
      s_x = l.index('S')
      start = (y, s_x)
      M[y][s_x] = 'S'
  
  
  assert start is not None
  traverse(lines, start, M)

  M = extend_map(M)
  flood(M)

  part2 = 0
  for y in range(len(M)):
    for x in range(len(M[y])):
      if M[y][x] == '.':
        part2 += 1
  
  print(part2)

  
  
