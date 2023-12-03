#!/usr/bin/python3
import os

def search_symbols(engine_map, y, x):
  for yy in range(y-1, y+2, 1):
    if yy < 0 or yy >= len(engine_map): continue
    for xx in range(x-1, x+2, 1):
      if xx < 0 or xx >= len(engine_map[yy]): continue
      p = engine_map[yy][xx]
      if p != '.' and not p.isdigit():
        return True
  
  return False

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()

  part1 = 0
  
  buf = ''
  c_buf = []
  gears = []
  numbers = []
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      c = lines[y][x]
      if c.isdigit():
        buf += c
        c_buf.append((y, x))
      else:
        for ia, a in enumerate(c_buf):
          if search_symbols(lines, a[0], a[1]):
            part1 += int(buf)
            numbers.append((int(buf), c_buf)) # part 2
            break
        buf = ''
        c_buf = []
  
  # Part 2
  part2 = 0
  gears = []
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      c = lines[y][x]
      if c == '*':
        gears.append([y,x,1])

  for (y,x,ratio) in gears:
    found_numbers = set()
    nn = [
      (y-1, x-1),
      (y-1, x),
      (y-1, x+1),
      (y, x-1),
      (y, x),
      (y, x+1),
      (y+1, x-1),
      (y+1, x),
      (y+1, x+1)
    ]
    for number in numbers:
      for n in nn:
        if n in number[1]: found_numbers.add(number[0])
    if len(found_numbers) == 2:
      part2 += found_numbers.pop() * found_numbers.pop()

        


  print(part1)
  print(part2)
  