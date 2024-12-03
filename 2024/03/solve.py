import os
import re

def part2(lines):
  result = 0
  do = True
  for line in lines:
    founds = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
    for x in founds:
      if x.startswith('don'):
        do = False
      elif x.startswith('do'):
        do = True
      elif do:
        a,b = (int(xx) for xx in re.findall('\d+', x))
        result += a * b

  return result

def part1(lines):
  result = 0

  for line in lines:
    founds = re.findall(r'mul\(\d+,\d+\)', line)
    for x in founds:
      a,b = (int(xx) for xx in re.findall('\d+', x))
      result += a * b

  return result


with open(os.path.dirname(__file__) + '/input') as f:
  lines = f.read().splitlines()

  print(part1(lines))
  print(part2(lines))