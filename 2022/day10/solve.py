#!/usr/local/bin/python3

def flatten(l):
    return [item for sublist in l for item in sublist]


with open('./input.txt') as f:
    lines = f.read().splitlines()
    lines_mapped = flatten(list(map(lambda x: x.split(' '), lines)))
    output = []

    x = 1
    score = 0
    line_output = ''
    lines_mapped.append('noop')
    for i, line in enumerate(lines_mapped):
        # part 1
        cycle = i + 1
        if (cycle+20) % 40 == 0 or cycle == 20:
            score += cycle * x

        # part 2
        screen_position = i % 40
        if screen_position % 40 == 0 and i != 0:
            output.append(line_output)
            line_output = ''
        if screen_position in range(x-1, x+2):
            line_output += '#'
        else:
            line_output += '.'

        if line == 'noop' or line == 'addx':
            continue
        x += int(line)

    for line in output:
        print(line)
    print(score)
