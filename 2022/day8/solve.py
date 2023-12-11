#!/usr/local/bin/python3

def check_left(trees, x, y):
    highest_left = 0
    for i in range(x-1, -1, -1):
        tree = int(trees[y][i])
        if tree >= highest_left:
            highest_left = tree

    return highest_left < int(trees[y][x])


def check_right(trees, x, y):
    highest = 0
    if x == 2 and y == 2:
        print('xd')
    for i in range(x+1, len(trees[y])):
        tree = int(trees[y][i])
        if tree >= highest:
            highest = tree

    return highest < int(trees[y][x])


def check_top(trees, x, y):
    highest = 0
    for i in range(y-1, -1, -1):
        tree = int(trees[i][x])
        if tree >= highest:
            highest = tree

    return highest < int(trees[y][x])

def check_bottom(trees, x, y):
    highest = 0
    for i in range(y+1, len(trees)):
        tree = int(trees[i][x])
        if tree >= highest:
            highest = tree

    return highest < int(trees[y][x])


def visible_check(trees, x, y):
    return (
        check_top(trees, x, y) or check_bottom(trees, x, y) or check_left(trees, x, y) or check_right(trees, x, y)
    )


with open('./input.txt') as f:
    lines = f.read().splitlines()
    trees = list(map(lambda x: list(x), lines))

    visible = (2 * len(lines)) + (2 * len(trees) - 4)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            is_visible = visible_check(trees, x, y)
            if is_visible:
                visible += 1
    print(visible)

