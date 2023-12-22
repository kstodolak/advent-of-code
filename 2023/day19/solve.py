#!/usr/bin/python3
import os, re

with open(os.path.dirname(__file__) + "/input.txt") as f:
  lines = f.read().splitlines()
  workflows = dict()
  parts = []

  while lines:
    curr = lines.pop(0)
    if curr == "":
      break
    name, rest = curr.split("{") 
    rest = rest.replace("}", "")
    rest = rest.split(",")
    workflows[name] = rest

  accepted = []
  parts = []
  for i, line in enumerate(lines):
    part = tuple(map(int, re.findall(r"\w=(-?\d+)", line)))
    parts.append(part)
    w_id = "in"
    while True:
      if w_id == "A":
        accepted.append(i)
        break
      if w_id == "R":
        break
      workflow = workflows[w_id]
      finished = False
      for w in workflow:
        if w.isalnum():
            w_id = w
            break
        w1, w2 = w.split(":")
        tmp = -1
        if w1[0] == "x":
            tmp = 0
        if w1[0] == "m":
            tmp = 1
        if w1[0] == "a":
            tmp = 2
        if w1[0] == "s":
            tmp = 3
        exp = f"part[{tmp}]" + w1[1:]
        if eval(exp):
            w_id = w2
            break
  part1 = 0
  for i in accepted:
      part1 += sum(parts[i])
  print(part1)
