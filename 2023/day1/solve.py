#!/usr/bin/python3
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  print(lines)