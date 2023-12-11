#!/usr/local/bin/python3
import re
import collections

REGEXP = r"(\w+) (\d+) (\w+) (\d+) (\w+) (\d+)"

def move(stacks, from_index, to_index, quantity):
    for i in range(quantity):
        el = stacks[from_index].pop()
        stacks[to_index].append(el)


def move_same_order(stacks, from_index, to_index, quantity):
    stack_tmp = []
    for i in range(quantity):
        el = stacks[from_index].pop()
        stack_tmp.append(el)
    while len(stack_tmp) > 0:
        el = stack_tmp.pop()
        stacks[to_index].append(el)


with open('./input.txt') as f:
    lines = f.read().splitlines()
    stacks_a = collections.defaultdict(lambda: [])
    stacks_b = collections.defaultdict(lambda: [])

    empty_index = lines.index('')
    stack_input = lines[0:empty_index - 1]
    move_input = lines[empty_index + 1:]

    for line in stack_input:
        for i in range(0, len(line), 4):
            char = line[i:i + 4][1]
            if char != ' ':
                index = int(i/4)
                stacks_a[index].insert(0, char)
                stacks_b[index].insert(0, char)

    for command in move_input:
        (_, quantity, _, from_index, _, to_index) = re.match(
            REGEXP, command).groups()
        move(stacks_a, int(from_index) - 1, int(to_index) - 1, int(quantity))
        move_same_order(stacks_b, int(from_index) - 1, int(to_index) - 1, int(quantity))

    result_1 = ""
    result_2 = ""
    for i in range(len(stacks_a)):
        result_1 += stacks_a[i][-1]
        result_2 += stacks_b[i][-1]

    print(result_1)
    print(result_2)
