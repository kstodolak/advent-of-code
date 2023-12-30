#!/usr/bin/python3
import os, sys
from collections import defaultdict

G = None
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

POS_DIRECTIONS = {
  "^": [(-1, 0)],
  "v": [(1, 0)],
  ">": [(0, 1)],
  "<": [(0, -1)],
  ".": DIRECTIONS,
}

def find_graph_nodes(M):
  nodes = []
  for y, row in enumerate(M):
    for x, c in enumerate(row):
      if c == "#":
        continue

      n_count = 0
      for dy, dx in DIRECTIONS:
        ny = y + dy
        nx = x + dx
        if ny in range(len(M)) and nx in range(len(M[0])):
          cc = M[ny][nx]
          if cc != "#":
            n_count += 1

      if n_count > 2:
        nodes.append((y, x))
  return nodes

def create_graph(M, nodes, part2=False):
  graph = defaultdict(lambda: dict())

  for from_y, from_x in nodes:
    todo = [(0, from_y, from_x)]
    visited = set()

    while todo:
      (dist, y, x) = todo.pop()
      if (y, x) in visited:
        continue
      visited.add((y, x))
      if dist > 0 and (y, x) in nodes:
        graph[(from_y, from_x)][(y, x)] = dist
        continue

      c = M[y][x]
      dirs = DIRECTIONS if part2 else POS_DIRECTIONS[c]
      for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        if ny in range(len(M)) and nx in range(len(M[0])):
          cc = M[ny][nx]
          if cc != "#":
            todo.append((dist + 1, ny, nx))

  return graph

dfs_visited = set()

def dfs(p, end):
  if p == end:
    return 0
  max_dist = -sys.maxsize

  dfs_visited.add(p)
  for neigbor in G[p]:
    if neigbor not in dfs_visited:
      max_dist = max(max_dist, dfs(neigbor, end) + G[p][neigbor])

  dfs_visited.remove(p)

  return max_dist

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  start = (0, lines[0].index('.'))
  end = (len(lines)-1, lines[-1].index('.'))

  nodes = [start, end]
  nodes.extend(find_graph_nodes(lines))

  G = create_graph(lines, nodes, False) # part 1
  print(dfs(start, end))

  G = create_graph(lines, nodes, True) # part 2
  print('Part 2... (this may take a few seconds)')
  print(dfs(start, end))

  