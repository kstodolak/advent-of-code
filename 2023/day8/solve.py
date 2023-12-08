#!/usr/bin/python3
import os, re, math

def part1(nodes, rl, starting_node):
  my_node = starting_node
  i = 0
  while my_node != 'ZZZ':
    next_move = rl[i%len(rl)]
    (l,r) = nodes[my_node]

    if next_move == 'L':
      my_node = l
    else:
      my_node = r
    i+=1
  
  return i

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  rl = lines.pop(0)
  lines.pop(0)

  nodes = dict()
  for line in lines:
    node,left,right = re.findall(r'(\w+)', line)
    nodes[node] = (left,right)

  print(part1(nodes, rl, 'AAA'))
  starting = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
  
  my_nodes = [x for x in starting]
  i = 0
  x = []
  while True:
    next_move = rl[i%len(rl)]
    for ii, my_node in enumerate(my_nodes):
      (l,r) = nodes[my_node]

      my_nodes[ii] = l if next_move == 'L' else r
      if my_nodes[ii][-1] == 'Z':
        x.append(i+1)
    i+=1
    if len(x) == len(my_nodes): break
    # if all(n[-1] == 'Z' for n in my_nodes): break
  
  print(math.lcm(*x))

