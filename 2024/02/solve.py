import os

with open(os.path.dirname(__file__) + '/input') as f:
  lines = f.read().splitlines()

  levels = []
  for line in lines:
    _levels = list(int(x) for x in line.split())
    levels.append(_levels)

  part1 = 0
  for level in levels:
    safe = True
    diffs = []
    for i in range(1, len(level)):
      prev = level[i-1]
      curr = level[i]
      diff = curr - prev
      diffs.append(diff)

      if abs(diff) > 3:
        safe = False
        break

    same_direction = all(x > 0 for x in diffs) or all(x < 0 for x in diffs)
    if not same_direction:
      safe = False
    if safe:
      part1 += 1

    # print(level, safe)
  print(part1)