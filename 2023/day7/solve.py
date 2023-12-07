#!/usr/bin/python3
import os

# Without 'J'
CARDS_VALUE = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'Q': 12,
  'K': 13,
  'A': 14,
}

def card_value(c, part2):
  if c == 'J' and part2: return 1
  if c == 'J': return 11

  return CARDS_VALUE[c]

# Hand values
# 7 - Five of kind
# 6 - Four of kind
# 5 - Full house
# 4 - Three of kind
# 3 - Two pair
# 2 - One pair
# 1 - High card

def calc_value2(in_hand):
  jokers = in_hand['J'] if 'J' in in_hand else 0
  vls = in_hand.values()

  if 5 in vls: return 7
  if jokers == 4: return 7
  if jokers == 3 and 2 in vls: return 7
  if jokers == 2 and 3 in vls: return 7
  if jokers == 1 and 4 in vls: return 7

  if jokers == 3: return 6
  if jokers == 2 and list(vls).count(2) > 1: 
    return 6
  if jokers == 1 and 3 in vls: return 6 
  if 4 in vls: return 6

  if jokers == 1 and list(vls).count(2) > 1: return 5
  if 3 in vls and 2 in vls: return 5

  if 3 in vls: return 4
  if jokers == 2: return 4
  if jokers == 1 and 2 in vls: return 4

  if list(vls).count(2) > 1: return 3

  if 2 in vls: return 2
  if jokers == 1: return 2

  return 1

def calc_value(in_hand):
  vls = in_hand.values()
  if 5 in vls: return 7
  if 4 in vls: return 6
  if 3 in vls:
    if 2 in vls: return 5
    return 4
  if 2 in vls:
    if list(vls).count(2) > 1: return 3
    return 2
  return 1

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()
  hands = []
  for line in lines:
    (cards, bid) = line.split(' ')
    hands.append((cards, int(bid)))

  hands_valued = []
  hands_valued2 = []
  for (cards, bid) in hands:
    in_hand = dict()
    card_values = []
    card_values2 = []
    for c in cards:
      if c not in in_hand:
        in_hand[c] = 0
      in_hand[c] += 1
      card_values.append(card_value(c, False))
      card_values2.append(card_value(c, True))

    hands_valued.append((cards, bid, calc_value(in_hand), tuple(card_values))) # part1
    hands_valued2.append((cards, bid, calc_value2(in_hand), tuple(card_values2))) # part2
  
  hands_valued = sorted(hands_valued, key=lambda x: (x[2], x[3]))
  hands_valued2 = sorted(hands_valued2, key=lambda x: (x[2], x[3]))
  
  part1 = 0
  part2 = 0
  for i in range(1, len(hands_valued)+1,1):
    part1 += i * hands_valued[i-1][1]
    part2 += i * hands_valued2[i-1][1]

  print(part1)
  print(part2)

