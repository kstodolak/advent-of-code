import os
from collections import Counter
from copy import deepcopy


def part1(list1, list2):
  list1.sort()
  list2.sort()
  dist_sum = 0

  for i in range(len(list1)):
    dist_sum += abs(list1[i] - list2[i])

  return dist_sum

def part2(list1, list2):
  list2_counter = Counter(list2)

  sim_score = 0
  for i in list1:
    sim_score += i * list2_counter[i]

  return sim_score

with open(os.path.dirname(__file__) + '/input') as f:
  lines = f.read().splitlines()
  list1, list2 = [], []
  for line in lines:
    a, b = line.split('   ')
    list1.append(int(a))
    list2.append(int(b))

  dist_sum = 0

  for i in range(len(list1)):
    dist_sum += abs(list1[i] - list2[i])

  # Part1: 1873376
  print(part1(deepcopy(list1), deepcopy(list2)))

  # Part2: 18997088
  print(part2(list1, list2))




