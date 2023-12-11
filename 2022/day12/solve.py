#!/usr/local/bin/python3
import numpy as np


def in_range(graph, point):
    if point[0] not in range(0, len(graph)): return False
    if point[1] not in range(0, len(graph[point[0]])): return False
    return True


def get_height(graph, point):
    (y, x) = point
    el = graph[y][x]
    if el == 'S':
        return 96
    if el == 'E':
        return 123
    return ord(el)


def get_possible_directions(graph, point, visited):
    (y, x) = point
    h = get_height(graph, point)

    directions = [
        (y, x - 1),
        (y, x + 1),
        (y - 1, x),
        (y + 1, x)
    ]
    directions = list(filter(lambda point: in_range(graph, point), directions))
    directions = list(filter(lambda point: point not in visited, directions))
    directions = list(filter(lambda x: (get_height(graph, x) - h) <= 1, directions))
    return directions


def calc(graph, position):
    visited = set()
    to_go_list = [(position, 0)]

    while len(to_go_list):
        (point, step) = to_go_list.pop(0)
        if point in visited:
            continue
        visited.add(point)
        if graph[point] == 'E':
            return step
        next_directions = get_possible_directions(graph, point, visited)
        next_directions = list(map(lambda x: (x, step + 1), next_directions))
        to_go_list.extend(next_directions)

    return 0


with open('./input.txt') as f:
    lines = f.read().splitlines()
    graph = np.array([list(line) for line in lines])

    pos_s = np.where(graph == 'S')
    start_position = (pos_s[0][0], pos_s[1][0])
    # part 1
    print(calc(graph, start_position))

    # part 2
    lowest_points = zip(*np.where(graph == 'a'))
    paths = []
    print('Wait a feeeew seconds xd')
    for point in lowest_points:
        path = calc(graph, point)
        if path > 0:
            paths.append(path)

    print(min(paths))
