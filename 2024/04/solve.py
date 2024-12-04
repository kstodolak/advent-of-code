import os
from collections import Counter

PLUS_DIRECTIONS = [
  (0, 1), # right
  (1, 0), # down
  (0, -1), # left
  (-1, 0), # up
]

X_DIRECTIONS = [
  (1, 1), # down-right
  (1, -1), # down-left
  (-1, -1), # up-left
  (-1, 1), # up-right
]

ALL_DIRECTIONS = PLUS_DIRECTIONS + X_DIRECTIONS

def look_for_mas(y, x, dy, dx, chars):
  if y + (3 * dy) < 0 or y + (3 * dy) >= len(chars):
    return False

  if x + (3 * dx) < 0 or x + (3 * dx) >= len(chars[0]):
    return False

  look_for = ['M', 'A', 'S']
  for i, c in enumerate(look_for, start=1):
    if chars[y + i * dy][x + i * dx] != c:
      return False

  return True

def get_char(y, x, chars):
  if y < 0 or y >= len(chars):
    return None
  if x < 0 or x >= len(chars[0]):
    return None

  return chars[y][x]

def find_xmas(y, x, chars):
  count = 0
  for dy, dx in ALL_DIRECTIONS:
    if look_for_mas(y, x, dy, dx, chars):
      count += 1

  return count

def find_x__mas(y, x, chars):
  neighbors = []
  for dy, dx in X_DIRECTIONS:
    neighbors.append(get_char(y + dy, x + dx, chars))
  neighbors_counter = Counter(neighbors)
  if neighbors_counter['M'] != 2 or neighbors_counter['S'] != 2:
    return False
  if neighbors[0] != neighbors[2]:
    return True

  return False

def part1(chars):
  result = 0
  for y, line in enumerate(chars):
    for x, c in enumerate(line):
      if c == 'X':
        result += find_xmas(y, x, chars)

  return result

def part2(chars):
  result = 0
  for y, line in enumerate(chars):
    for x, c in enumerate(line):
      if c == 'A':
        result += 1 if find_x__mas(y, x, chars) else 0

  return result

with open(os.path.dirname(__file__) + '/input') as f:
  lines = f.read().splitlines()
  chars = [list(x) for x in lines]

  print(part1(chars))
  print(part2(chars))
