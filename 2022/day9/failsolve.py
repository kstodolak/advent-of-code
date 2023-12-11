#!/usr/local/bin/python3
from operator import countOf


def simulate_path(prev, target, positions_visited=None):
    if positions_visited is None:
        positions_visited = []
    (p_x, p_y) = prev
    (t_x, t_y) = target
    d_x = t_x - p_x
    d_y = t_y - p_y
    if abs(d_x) > 1 or abs(d_y) > 1:
        if abs(d_x) == 1:
            if d_y > 0:
                for i in range(p_y + 1, t_y, 1):
                    positions_visited.append((t_x, i))
            else:
                for i in range(p_y - 1, t_y, -1):
                    positions_visited.append((t_x, i))
        elif d_x == 0:
            step = 1 if d_y > 0 else -1
            for i in range(p_y + step, t_y, step):
                positions_visited.append((t_x, i))
        elif d_y == 0:
            step = 1 if d_x > 0 else -1
            for i in range(p_x + step, t_x, step):
                positions_visited.append((i, t_y))
        else:
            if d_x > 0:
                for i in range(p_x + 1, t_x, 1):
                    positions_visited.append((i, t_y))
            else:
                for i in range(p_x - 1, t_x, -1):
                    positions_visited.append((i, t_y))
    return positions_visited

with open('./input.txt') as f:
    lines = f.read().splitlines()

    # start 0, 0
    (t_pos_x, t_pos_y) = 0, 0
    last_move = 'R'
    last_move_direction = 'H'

    directions = {'R': 'H', 'L': 'H', 'U': 'V', 'D': 'V'}
    (h_pos_x, h_pos_y) = 0, 0
    h_visited = []  # (x, y): 0
    for line in lines:
        (move, s) = line.split(' ')
        step = int(s)
        if move == 'L':
            h_pos_x -= step
        if move == 'R':
            h_pos_x += step
        if move == 'U':
            h_pos_y -= step
        if move == 'D':
            h_pos_y += step
        h_visited.append((h_pos_x, h_pos_y))

    t_x = 0
    t_y = 0
    t_visited = [(0, 0)]
    for (h_x, h_y) in h_visited:
        d_x = h_x - t_x
        d_y = h_y - t_y
        if abs(d_x) > 1 or abs(d_y) > 1:
            result_arr = simulate_path((t_x, t_y), (h_x, h_y))
            (n_x, n_y) = result_arr[-1]
            t_x = n_x
            t_y = n_y
            t_visited.extend(result_arr)

    set_t_visited = set(t_visited)
    # print(set_t_visited)

    # print(t_visited)
    # duplicates = list(filter(lambda x: countOf(t_visited, x), list(set_t_visited)))

    # print(len(t_visited) - len(set_t_visited))
    print(len(set_t_visited))