#!/usr/bin/python3
import os, re
import numpy as np

A = lambda *a: np.array(a) # np array for adding array like [0,0,0,0] + [1,2,3,4] = [1,2,3,4]

key = lambda a: tuple(a[0]+a[1]) + tuple(a[1]) # updated resources and robots
get_best = lambda x: sorted(np.unique(x, axis=0), key=key)[-1800:] # get best combo value + robots

def run(blueprint, time):
  todo = [(A(0,0,0,0), A(0,0,0,1))] # (resources, robots)
  for t in range(time, 0, -1):
    tmp_todo = list()
    for (resources, robots) in todo:
      tmp_todo.append((resources+robots, robots))
      for (cost, to_add) in blueprint:
        if all(cost <= resources):
          tmp_todo.append((resources-cost+robots,  robots + to_add))
    todo = get_best(tmp_todo)
  
  return max(resources[0] for (resources, _) in todo)

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  part1 = 0
  part2 = 1
  for line in lines:
    (i, a, b, c_1, c_2, d_1, d_2) = map(int, re.findall(r'\d+', line))
    blueprint = [
      (A(0,0,0,a), A(0,0,0,1)), #     ore robot cost a ore
      (A(0,0,0,b), A(0,0,1,0)), #     clay robot cost b ore
      (A(0,0,c_2,c_1), A(0,1,0,0)), # obsidian robot cost c_2 clay and c_1 ore
      (A(0,d_2,0,d_1), A(1,0,0,0)), # geode robot cost d_2 obsidian and d_1 ore
    ]

    part1 += run(blueprint, 24) * i
    if i < 4:
      part2 *= run(blueprint, 32)
  
  print(part1, part2)