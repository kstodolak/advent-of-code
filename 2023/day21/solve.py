#!/usr/bin/python3
import os
from collections import deque

MAP = None

def solve_part1(start, max_steps=64):
  todo = deque([(start[0], start[1], max_steps)])
  seen = set()
  result = set()
  while todo:
    curr = todo.popleft()
    (y, x, steps) = curr
    if (y, x) in seen: continue
    seen.add((y, x))

    if steps % 2 ==    0:
      result.add((y, x))
    
    if steps == 0: continue

    for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      yy = (y + dy)
      xx = (x + dx)
      if yy not in range(len(MAP)) or xx not in range(len(MAP)): continue
      if MAP[yy][xx] == '#': continue
      todo.append((yy, xx, steps - 1))
  
  return len(result)

f = open(os.path.dirname(__file__) + '/input.txt')

MAP = f.read().splitlines()
START = None

for y, line in enumerate(MAP):
  for x, c in enumerate(line):
    if c == 'S': START = (y,x)

# part 1
print(solve_part1(START))

# part 2
MAX_STEPS = 26501365
SIZE = len(MAP)
INTERSECTION_COUNT = MAX_STEPS / SIZE

# 1. grid is square
assert SIZE == len(MAP[0])
# 2. steps and size is odd
assert MAX_STEPS % 2 == 1 and SIZE % 2 == 1
# 3. starting on middle
assert START[0] == SIZE // 2 and START[1] == SIZE // 2 
# 4. horizontal, vertical lines from start are empty
# 5. steps number are multiply of steps + steps/2
assert (MAX_STEPS - MAX_STEPS) % SIZE == 0

grids_width = MAX_STEPS // SIZE - 1

odd = grids_width ** 2
even = (grids_width + 1) ** 2

odd_grids = solve_part1(START, SIZE * 2 + 1) # steps enough to reach every point in the map
even_grids = solve_part1(START, SIZE * 2)

grid_top = solve_part1((SIZE - 1, START[1]), SIZE-1)
grid_bottom = solve_part1((0, START[1]), SIZE-1)
grid_left = solve_part1((START[0], SIZE-1), SIZE - 1)
grid_right = solve_part1((START[0], 0), SIZE - 1)

triangle_small_NE = solve_part1((SIZE-1, 0), SIZE // 2 - 1)
triangle_small_NW = solve_part1((SIZE-1, SIZE-1), SIZE // 2 - 1)
triangle_small_SW = solve_part1((0, SIZE-1), SIZE // 2 - 1)
triangle_small_SE = solve_part1((0, 0), SIZE // 2 - 1)

triangle_big_NE = solve_part1((SIZE-1, 0), SIZE*3 // 2 - 1)
triangle_big_NW = solve_part1((SIZE-1, SIZE-1), SIZE*3 // 2 - 1)
triangle_big_SW = solve_part1((0, SIZE-1), SIZE*3 // 2 - 1)
triangle_big_SE = solve_part1((0, 0), SIZE*3 // 2 - 1)

part2 = (
  odd * odd_grids +
  even * even_grids +
  grid_top + grid_bottom + grid_left + grid_right +
  (grids_width + 1) * (triangle_small_NE + triangle_small_NW + triangle_small_SE + triangle_small_SW) +
  (grids_width) * (triangle_big_NE + triangle_big_NW + triangle_big_SE + triangle_big_SW) 
)

print(part2)