#!/usr/local/bin/python3

# 0 -  9
def check_left(trees, x, y):
    if x == 0:
        return 0
    my_tree = int(trees[y][x])
    counter = 0
    for i in range(x-1, -1, -1):
        tree = int(trees[y][i])
        counter += 1
        if tree >= my_tree:
            return counter
    return counter


def check_right(trees, x, y):
    if x == (len(trees[y]) - 1):
        return 0
    my_tree = int(trees[y][x])
    counter = 0
    for i in range(x+1, len(trees[y])):
        tree = int(trees[y][i])
        counter += 1
        if tree >= my_tree:
             return counter
    return counter


def check_top(trees, x, y):
    if y == 0:
        return 0
    my_tree = int(trees[y][x])
    counter = 0
    for i in range(y-1, -1, -1):
        tree = int(trees[i][x])
        counter += 1
        if tree >= my_tree:
            return counter
    return counter


def check_bottom(trees, x, y):
    if y == (len(trees) - 1):
        return 0
    my_tree = int(trees[y][x])
    counter = 0
    for i in range(y+1, len(trees)):
        tree = int(trees[i][x])
        counter += 1
        if tree >= my_tree:
            return counter
    return counter


def get_scenic_score(trees, x, y):
    top = check_top(trees, x, y)
    bottom = check_bottom(trees, x, y)
    left = check_left(trees, x, y)
    right = check_right(trees, x, y)

    return top * right * left * bottom


with open('./input.txt') as f:
    lines = f.read().splitlines()
    trees = list(map(lambda x: list(x), lines))

    # Part 2
    highest_scenic_score = 0
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            score = get_scenic_score(trees, x, y)
            if score > highest_scenic_score:
                highest_scenic_score = score

    print(highest_scenic_score)