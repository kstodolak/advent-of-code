#!/usr/bin/python3
import os,re,sys

DIRECTIONS = {
'R': (0,1),
'D': (1,0),
'L': (0,-1),
'U': (-1,0)
}

def parse_input(lines):
  operations_1 = []
  operations_2 = []

  for line in lines:
    direction, count, color = line.split(' ')
    operations_1.append((direction, int(count)))

    color = color.replace('(', '').replace(')', '')
    count = int(color[1:-1], 16)
    dir_c = color[-1]
    direction = 'U'
    if dir_c == '0': direction = 'R'
    if dir_c == '1': direction = 'D'
    if dir_c == '2': direction = 'L'
    operations_2.append((direction, int(count)))
  
  return operations_1, operations_2

def polygon_area(operations):
  y = x = 1
  points = [(1,1)]
  counter = 0
  for (direction, count) in operations:
    counter += count
    (dy, dx) = DIRECTIONS[direction]
    y = y + count * dy
    x = x + count * dx
    points.append((y, x))
  
  result = 0
  for i in range(len(points)-1):
    p1 =  points[i]
    p2 = points[i+1]
    result += (p1[0] * p2[1]) - (p1[1] * p2[0])
  
  return abs(result) // 2 + counter//2 + 1


with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  (operations_1, operations_2) = parse_input(lines)

  # part1
  print(polygon_area(operations_1))
  # part2
  print(polygon_area(operations_2))