#!/usr/local/bin/python3

# A - X - Rock
# B - Y - Paper
# C - Z - Scissors

# X - Lose
# Y - Draw
# Z - Win

def calc_score(opp_move, my_move):
    score = {'X': 1, 'Y': 2, 'Z': 3}[my_move]

    score += {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }[(opp_move, my_move)]

    return score


def guess_move(opp_move, expected_score):
    my_move = {
        ('A', 'X'): 'Z', ('A', 'Y'): 'X', ('A', 'Z'): 'Y',
        ('B', 'X'): 'X', ('B', 'Y'): 'Y', ('B', 'Z'): 'Z',
        ('C', 'X'): 'Y', ('C', 'Y'): 'Z', ('C', 'Z'): 'X',
    }[(opp_move, expected_score)]

    return calc_score(opp_move, my_move)


with open('./input.txt') as f:
    lines = f.read().splitlines()

    score1 = 0
    score2 = 0
    for line in lines:
        opp, me = line.split(' ')
        score1 += calc_score(opp, me)
        score2 += guess_move(opp, me)

    print(score1)
    print(score2)
