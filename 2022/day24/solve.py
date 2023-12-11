#!/usr/local/bin/python3
import functools

INPUT_FILE = './input.txt'

@functools.cache
def is_not_blizzard(point, t):
    blizzards = simulate_blizzard_next_minute(t)
    return point not in blizzards


def simulate_blizzard_next_minute(t):
    if t < len(BLIZZARD_BY_TIME):
        return BLIZZARD_BY_TIME_POINTS[t]

    prev = BLIZZARD_BY_TIME[-1]
    blizzards = []
    bad_points = set()
    for b in prev:
        (p, y, x) = b
        (ny, nx) = (y, x)
        if p == '<':
            nx = x - 1
            if nx == 0:
                nx = (nx - 1) % (RIGHT_BORDER - 1)
        elif p == '>':
            nx = x + 1
            if nx == RIGHT_BORDER - 1:
                nx = (nx + 1) % (RIGHT_BORDER - 1)
        elif p == '^':
            ny = y - 1
            if ny == 0:
                ny = (ny - 1) % (BOTTOM_BORDER - 1)
        elif p == 'v':
            ny = y + 1
            if ny == BOTTOM_BORDER - 1:
                ny = (ny + 1) % (BOTTOM_BORDER - 1)
        else:
            assert False, p
        blizzards.append((p, ny, nx))
        bad_points.add((ny, nx))
    BLIZZARD_BY_TIME.append(blizzards)
    BLIZZARD_BY_TIME_POINTS.append(bad_points)
    return BLIZZARD_BY_TIME_POINTS[t]


def simulate(start, end, start_at=0):
    min_time = None
    queue = [(start[0], start[1], start_at)]  # y, x, time
    seen = set()
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr in seen:
            continue
        seen.add(curr)

        (cy, cx, ct) = curr
        next_time = ct + 1

        # check success
        if (cy, cx) == end:
            if min_time is None:
                min_time = ct
            else:
                min_time = min(min_time, ct)
            continue

        if min_time is not None and ct > min_time:
            continue

        # possible moves
        if cy != 0 and cy != (BOTTOM_BORDER - 1):
            left = (cy, cx - 1)
            if cx > 1 and is_not_blizzard(left, next_time):
                queue.append((*left, next_time))

            right = (cy, cx + 1)
            if cx < (RIGHT_BORDER - 2) and is_not_blizzard(right, next_time):
                queue.append((*right, next_time))

        up = (cy - 1, cx)
        if (cy > 1 or up == end) and is_not_blizzard(up, next_time):
            queue.append((*up, next_time))

        down = (cy + 1, cx)
        if (cy < (BOTTOM_BORDER - 2) or down == end) and is_not_blizzard(down, next_time):
            queue.append((*down, next_time))

        wait = (cy, cx)
        if is_not_blizzard(wait, next_time):
            queue.append((*wait, next_time))

    return min_time


with open(INPUT_FILE) as f:
    lines = f.read().splitlines()
    global BLIZZARD_BY_TIME  # (blizzard_direction, y, x)
    global BLIZZARD_BY_TIME_POINTS  # (y, x)
    global RIGHT_BORDER
    global BOTTOM_BORDER

    BOTTOM_BORDER = len(lines)
    RIGHT_BORDER = len(lines[0])
    blizzards = []
    blizzards_points = set()

    for y, line in enumerate(lines):
        for x, p in enumerate(line):
            if y == 0 and p == '.':
                start = (y, x)
            if y == (len(lines) - 1) and p == '.':
                end = (y, x)
            if p in ['>', 'v', '<', '^']:
                blizzards.append((p, y, x))
                blizzards_points.add((y, x))
    assert type(start) is tuple
    assert type(end) is tuple

    BLIZZARD_BY_TIME = [blizzards]
    BLIZZARD_BY_TIME_POINTS = [blizzards_points]

    result = simulate(start, end)  # Start -> goal
    print(result)  # part 1
    result2 = simulate(end, start, result)  # way back to start
    result3 = simulate(start, end, result2)  # Start -> goal again
    print(result3)  # part 2



