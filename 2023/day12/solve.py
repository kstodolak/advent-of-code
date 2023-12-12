#!/usr/bin/python3
import os, re
from itertools import product
from functools import cache

def check_combination(comb, expected):
  counter = []
  buff = 0
  for c in comb:
    if c == '.' and buff > 0:
      counter.append(buff)
    if c == '.': 
      buff = 0
      continue

    if c == '#': buff += 1
  if buff > 0: counter.append(buff)

  return counter == expected

def calc_group(group):
  (springs, expected) = group
  possibilites = []
  for s in springs:
    if s == '?':
      possibilites.append(['.', '#'])
    else:
      possibilites.append([s])

  combinations = list(product(*possibilites))
  result = 0
  for comb in combinations:
    if check_combination(comb, expected): result += 1
  
  return result

springs = ""
groups_counts = []

@cache
def calc_group2(pos=0, curr_hash_group_len=-1, i_group=0):
  # curr_hash_group_len = -1 means previous spring was dot ('.')
  global springs, groups_counts
  if pos == len(springs):
    if curr_hash_group_len <= 0 and i_group == len(groups_counts): return 1
    else: return 0
  
  count = 0
  for s in ['#', '.']:
    if springs[pos] == '?' or springs[pos] == s:
      if s == '#': # hash or '?' replaced by hash
        if curr_hash_group_len > 0: # go with hash and countdown group count
          count += calc_group2(pos + 1, curr_hash_group_len-1, i_group)
        elif curr_hash_group_len < 0 and i_group < len(groups_counts): # previous was dot go next position with hash and start countdown next group
          count += calc_group2(pos+1, groups_counts[i_group]-1, i_group + 1)
      else: # dot or '?' replaced by dot
        if curr_hash_group_len <= 0: # If false, current recurence is wrong
          count += calc_group2(pos+1, -1, i_group)
  
  return count


with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  part1 = 0
  part2 = 0
  for line in lines:
    a,b = line.split(' ')
    b = list(map(int, b.split(',')))

    part1 += calc_group((a, b))

    springs = "?".join([a] * 5)
    groups_counts = b * 5
    calc_group2.cache_clear()
    part2 += calc_group2(0,-1,0)


  print(part1)
  print(part2)