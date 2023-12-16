#!/usr/bin/python3
import os

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

def traverse(M, start):
  ENERGIZED = set()
  todo = [(start[0], start[1], start[2])]
  visited = set()

  while todo:
    curr = todo.pop(0)
    if curr in visited: continue
    visited.add(curr)
    (y, x, direction) = curr
    if y not in range(0, len(M)) or x not in range(0, len(M[0])): continue

    ENERGIZED.add((y,x))
    tile = M[y][x]

    next_direction = []
    if tile == '.':
      next_direction.append(direction)
    elif tile == '\\':
      if direction == RIGHT: next_direction.append(DOWN)
      elif direction == UP: next_direction.append(LEFT)
      elif direction == DOWN: next_direction.append(RIGHT)
      elif direction == LEFT: next_direction.append(UP)
      else: assert False
    elif tile == '/':
      if direction == RIGHT: next_direction.append(UP)
      elif direction == UP: next_direction.append(RIGHT)
      elif direction == DOWN: next_direction.append(LEFT)
      elif direction == LEFT: next_direction.append(DOWN)
      else: assert False
    elif tile == '|':
      if direction in [RIGHT, LEFT]: next_direction.extend([UP, DOWN])
      elif direction in [UP, DOWN]: next_direction.append(direction)
      else: assert False 
    elif tile == '-':
      if direction in [RIGHT, LEFT]: next_direction.append(direction)
      elif direction in [UP, DOWN]: next_direction.extend([LEFT, RIGHT])
      else: assert False
    else: assert False

    for nxt in next_direction:
      (dy, dx) = nxt
      todo.append((y + dy, x + dx, nxt))
  
  return len(ENERGIZED)


with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  M = []
  start = (0,0)
  for line in lines:
    row = [l for l in line]
    M.append(row)
  
  part1 = traverse(M, (0,0, RIGHT))
  print(part1)
  
  part2 = 0    
  h = len(M)
  w = len(M[0])
  for y in range(len(M)):
    part2 = max(part2, traverse(M, (y,   0, RIGHT)))
    part2 = max(part2, traverse(M, (y, w-1, LEFT)))
  
  for x in range(len(M[0])):
    part2 = max(part2, traverse(M, (0,   x,   DOWN)))
    part2 = max(part2, traverse(M, (h-1, x, UP)))
  
  print(part2)

