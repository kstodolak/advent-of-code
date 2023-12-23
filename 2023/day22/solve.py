#!/usr/bin/python3
import os, re, sys
import operator
from collections import defaultdict, deque

bricks = []


# end1 >= start2 and end2 >= start1
def is_xy_overlaping(a, b):
    range_xa = (a[0], a[3])
    range_xb = (b[0], b[3])
    range_ya = (a[1], a[4])
    range_yb = (b[1], b[4])

    return (
        range_xa[1] >= range_xb[0]
        and range_xb[1] >= range_xa[0]
        and range_ya[1] >= range_yb[0]
        and range_yb[1] >= range_ya[0]
    )


def fall():
    for i, brick in enumerate(bricks):
        max_z = 0
        for next_brick in bricks[:i]:  # check under
            if is_xy_overlaping(brick, next_brick):
                max_z = max(max_z, next_brick[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z


with open(os.path.dirname(__file__) + "/input.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        l = line.replace("~", ",").split(",")
        l = list(map(int, l))
        bricks.append(l)

    bricks.sort(key=operator.itemgetter(2))
    fall()
    bricks.sort(key=operator.itemgetter(2))

    supports = defaultdict(lambda: set())
    supported_by = defaultdict(lambda: set())

    for i, brick in enumerate(bricks):
        for j, under_brick in enumerate(bricks[:i]):
            if is_xy_overlaping(brick, under_brick) and brick[2] == under_brick[5] + 1:
                supports[j].add(i)  # j supports i
                supported_by[i].add(j)  # i is supported by j

    part1 = 0
    not_safe = set()
    for i in range(len(bricks)):
        ok = True  # all bricks supported by i have more than 1 supporters
        for j in supports[i]:
            if len(supported_by[j]) < 2:
                ok = False
                break
        if ok:
            part1 += 1
        else:
            not_safe.add(i)

    print(part1)

    part2 = 0
    for i in not_safe:
        todo = deque()
        for j in supports[i]:
            if len(supported_by[j]) == 1:
                todo.append(j)
        will_fall = set(todo)
        part2 += len(will_fall)
        will_fall.add(i)

        while todo:
            curr = todo.popleft()
            for j in supports[curr] - will_fall:
                if supported_by[j].issubset(will_fall):
                    todo.append(j)
                    will_fall.add(j)
                    part2 += 1

    print(part2)
