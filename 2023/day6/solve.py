#!/usr/bin/python3
import os,re

def calculate_distance(hold,time):
  time_left = time-hold
  speed=hold
  dist=0
  for t in range(time_left):
    dist += speed
  return dist


with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  times = list(map(int,re.findall(r'\d+', lines[0])))
  distances = list(map(int,re.findall(r'\d+', lines[1])))

  record_beaten = [0 for x in times]
  for i,time in enumerate(times):
    max_distance=0
    for t in range(time):
      dist = t * (time-t)
      if dist >= max_distance: 
        max_distance = dist
      if dist > distances[i]: 
        record_beaten[i] += 1


  part1=1
  for x in record_beaten:
    part1 *= x
  print(part1)