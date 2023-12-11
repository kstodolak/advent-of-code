#!/usr/local/bin/python3

def get_range_limiters(input_line):
    return [
        list(map(int, input_line[0].split('-'))),
        list(map(int, input_line[1].split('-'))),
    ]


with open('./input.txt') as f:
    lines = f.read().splitlines()

    mapped_lines = list(map(lambda line: line.split(','), lines))
    mapped_lines_2 = mapped_lines.copy()

    # part 1
    count_1 = 0
    for line in mapped_lines:
        (range_1, range_2) = get_range_limiters(line)

        if range_1[0] >= range_2[0] and range_1[1] <= range_2[1]:
            count_1 += 1
        elif range_2[0] >= range_1[0] and range_2[1] <= range_1[1]:
            count_1 += 1

    # part 2
    count_2 = 0
    for line in mapped_lines_2:
        (range_1, range_2) = get_range_limiters(line)

        if range_2[0] <= range_1[0] <= range_2[1]:
            count_2 += 1
        elif range_1[0] <= range_2[0] <= range_1[1]:
            count_2 += 1

    print(count_1)
    print(count_2)
