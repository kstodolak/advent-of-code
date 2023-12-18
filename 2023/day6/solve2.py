#!/usr/bin/python3
import os,re

def calculate_distance(hold,time):
  time_left = time-hold
  speed=hold
  dist=0
  for t in range(time_left):
    dist += speed
  return dist

def find_break(time, record):
  lo = 0
  hi = time // 2

  while lo+1 < hi:
    m = (lo+hi) // 2
    d = m * (time - m)
    if d >= record:
      hi = m
    else: 
      lo = m
  
  return hi

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = list(map(lambda x: x.replace(' ', ''), f.read().splitlines()))
  time = list(map(int,re.findall(r'\d+', lines[0])))[0]
  distance = list(map(int,re.findall(r'\d+', lines[1])))[0]

  record_beaten = 0
  time_to_record = find_break(time, distance)
  
  print(time-(2*time_to_record)+1)