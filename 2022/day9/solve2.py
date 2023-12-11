#!/usr/local/bin/python3


def get_new_position(head, tail):
    (h_x, h_y) = head
    (t_x, t_y) = tail
    (n_x, n_y) = tail
    # d_x > 0 -> Right
    # d_x < 0 -> Left
    # d_y > 0 -> Down
    # d_y < 0 -> Up
    d_x = h_x - t_x
    d_y = h_y - t_y

    if abs(d_x) > 1 or abs(d_y) > 1:
        # if x distance < 2 take x of head else take x +/- 1
        n_x = (h_x - 1 if d_x > 0 else h_x + 1) if abs(d_x) > 1 else h_x
        # if y distance < 2 take y of head else take y +/- 1
        n_y = (h_y - 1 if d_y > 0 else h_y + 1) if abs(d_y) > 1 else h_y

    return n_x, n_y


with open('./input.txt') as f:
    lines = f.read().splitlines()

    h_x, h_y = (0, 0)
    t_visited = [[(0, 0)] for _ in range(9)]

    for line in lines:
        (move, s) = line.split(' ')
        step = int(s)
        for i in range(step):
            if move == 'L':
                h_x -= 1
            if move == 'R':
                h_x += 1
            if move == 'U':
                h_y -= 1
            if move == 'D':
                h_y += 1
            t_visited[0].append(get_new_position((h_x, h_y), t_visited[0][-1]))

    for i in range(1, 9):
        for j in range(len(t_visited[i-1])):
            t_visited[i].append(get_new_position(t_visited[i-1][j], t_visited[i][j]))

    print(len(set(t_visited[0])))
    print(len(set(t_visited[8])))
