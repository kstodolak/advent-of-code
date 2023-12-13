#!/usr/bin/python3
import os
import numpy as np

def find_vertical(board, max_wrong=0):
  mirror_points = []
  for x in range(len(board[0])-1):
    if np.count_nonzero(board[:,x] != board[:,x+1]) <= max_wrong:
      mirror_points.append(x+1)

  max_x = 0
  for m in mirror_points:
    i = m - 1
    x = m
    wrongs = 0
    while i >= 0 and x < len(board[0]):
      w = np.count_nonzero(board[:,x] != board[:,i])
      wrongs += w
      i -= 1
      x += 1
    if wrongs == max_wrong and m > max_x:
      max_x = m

  return max_x


def find_horizontal(board, max_wrong=0):
  mirror_points = []
  for y in range(len(board)-1):
    if np.count_nonzero(board[y, :] != board[y+1,:]) <= max_wrong:
      mirror_points.append(y+1)
  
  max_y = 0
  for m in mirror_points:
    i = m - 1
    y = m
    wrongs = 0
    finished = True
    while i >= 0 and y < len(board):
      w = np.count_nonzero(board[y, :] != board[i,:])
      wrongs += w
      i -= 1
      y += 1
    if wrongs == max_wrong and m > max_y:
      max_y = m
  
  return max_y

def calc_board(board, part2=False):
  vertical = find_vertical(board, 1 if part2 else 0)
  horizontal = find_horizontal(board, 1 if part2 else 0)
  if vertical > 0:
    return vertical
  else:
    return horizontal * 100


with open(os.path.dirname(__file__) + '/input.txt') as f:
  patterns = f.read().split('\n\n')
  
  part1 = 0
  part2 = 0
  for xxx, pattern in enumerate(patterns):
    a = []
    for line in pattern.splitlines():
      row = []
      for c in line:
        row.append(c)
      a.append(row)
    board = np.where(np.array(a) == '#', 1, 0)
    part1 += calc_board(board)
    part2 += calc_board(board, True)
  
  print(part1) # 30802
  print(part2) # 37876

