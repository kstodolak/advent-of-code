import os

def is_save(diffs):
  if len(diffs) < 2:
    return False
  safe = all(abs(x) < 4 for x in diffs)
  all_up = all(x > 0 for x in diffs)
  all_down = all(x < 0 for x in diffs)
  same_direction = all_up or all_down
  if not same_direction:
    safe = False

  return safe

with open(os.path.dirname(__file__) + '/input') as f:
  lines = f.read().splitlines()

  levels = []
  for line in lines:
    _levels = list(int(x) for x in line.split())
    levels.append(_levels)

  part1 = 0
  part2 = 0
  for level in levels:
    diffs = []
    for i in range(1, len(level)):
      prev = level[i-1]
      curr = level[i]
      diff = curr - prev
      diffs.append(diff)

    safe = is_save(diffs)
    if safe:
      part1 += 1
      part2 += 1
    else:
      for i in range(len(level)):
        diffs = []
        _level = level[:i] + level[i+1:]
        for ii in range(1, len(_level)):
          prev = _level[ii-1]
          curr = _level[ii]
          diff = curr - prev
          diffs.append(diff)
        safe = is_save(diffs)
        if safe:
          part2 += 1
          break

  print(part1, part2)