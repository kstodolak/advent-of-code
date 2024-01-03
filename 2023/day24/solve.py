#!/usr/bin/python3
import os
import sympy
from itertools import combinations

SEARCH_RANGE_MIN = 200000000000000
SEARCH_RANGE_MAX = 400000000000000

def line_equation(x, y, z, vx, vy, vz):
  a = vy
  b = -vx
  c = vy * x - vx * y

  return [a, b, c]

def is_parallel(a1, b1, a2, b2):
  return a1 / b1 == a2 / b2

def solve_part1(hailstones):
  part1 = 0
  for h1, h2 in combinations(hailstones, 2):
    line_eq1 = line_equation(*h1)
    line_eq2 = line_equation(*h2)
    a1, b1, c1 = line_eq1
    a2, b2, c2 = line_eq2

    if is_parallel(a1, b1, a2, b2): continue

    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)

    if SEARCH_RANGE_MIN <= x <= SEARCH_RANGE_MAX and SEARCH_RANGE_MIN <= y <= SEARCH_RANGE_MAX:
      if (
        ((x-h1[0]) * h1[3] >= 0 and (y-h1[1]) * h1[4] >= 0) and
        ((x-h2[0]) * h2[3] >= 0 and (y-h2[1]) * h2[4] >= 0)
      ):
        part1 += 1
  
  return part1

with open(os.path.dirname(__file__) + '/input.txt') as f:
  input_lines = f.read().splitlines()
  hailstones = []

  for input_line in  input_lines:
    h = tuple(map(int, input_line.replace("@", ",").split(", ")))
    hailstones.append(h) # 0 - x, 1 - y, 2 - z, 3 - vx, 4 - vy, 5 - vz

  # print(solve_part1(hailstones))
  xr, yr, zr, vxr, vyr, vzr, t = sympy.symbols("xr, yr, zr, vxr, vyr, vzr, t")  
  equations = []
    
  for i, hailstone in enumerate(hailstones):
    x,y,z,vx,vy,vz = hailstone
    equations.append(sympy.Eq((xr - x) * (vy - vyr), (vx - vxr) * (yr - y)))
    equations.append(sympy.Eq((xr - x) * (vz - vzr), (vx - vxr) * (zr - z)))
    

  solutions = sympy.solve(equations)
  answer = solutions[0]
  part2 = answer[xr] + answer[yr] + answer[zr]
  print(part2)



    