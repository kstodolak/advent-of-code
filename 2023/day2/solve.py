#!/usr/bin/python3
import os, re

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  possible_cubes = [12, 13, 14] # red | green | blue

  part1 = 0
  part2 = 0
  for i, line in enumerate(lines, start=1):
    cubes = [0,0,0]
    search_results = re.findall(r'(\d+)\s(\w+)', line)

    for search_result in search_results:
      if search_result[1] == 'red': cubes[0] = max(int(search_result[0]), cubes[0])
      if search_result[1] == 'green': cubes[1] = max(int(search_result[0]), cubes[1])
      if search_result[1] == 'blue': cubes[2] = max(int(search_result[0]), cubes[2])
    
    if cubes[0] <= possible_cubes[0] and cubes[1] <= possible_cubes[1] and cubes[2] <= possible_cubes[2]: 
      part1 += i
    
    part2 += (cubes[0] * cubes[1] * cubes[2])
    
  print(part1)
  print(part2)