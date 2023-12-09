#!/usr/bin/python3
import os,re

def calc_differences(s):
  return [s[i] - s[i-1] for i in range(1, len(s))]

def predict_next(ds):
  sequence = ds
  prediction = 0

  while not all(x == 0 for x in sequence):
    prediction += sequence[-1]
    sequence = calc_differences(sequence)
  
  return prediction

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  
  data_sets = []
  for line in lines:
    data_sets.append(list(map(int, re.findall(r'-?\d+', line))))
  
  part1 = 0
  part2 = 0
  for ds in data_sets:
    part1 += predict_next(ds)
    part2 += predict_next(ds[::-1])

  print(part1)
  print(part2)