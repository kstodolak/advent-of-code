#!/usr/local/bin/python3
import collections
import re

COMMAND_REGEXP = r"move (\d+) from (\d+) to (\d+)"


def move(stack, from_index, to_index, quantity, keep_order = False):
    end_of_stack = len(stack[int(to_index) - 1])
    for i in range(int(quantity)):
        el = stack[int(from_index) - 1].pop(0)
        stack[int(to_index) - 1].insert(i if keep_order else 0, el)


with open('./input.txt') as f:
    lines = f.read().splitlines()
    empty_line_index = lines.index('')

    stack_a = collections.defaultdict(lambda: [])
    stack_b = collections.defaultdict(lambda: [])

    stack_input = list(map(lambda x: list(x[1::4]), lines[:empty_line_index - 1]))
    move_input = lines[empty_line_index + 1:]

    for line in stack_input:
        for i, el in enumerate(line):
            if el != ' ':
                stack_a[i].append(el)
                stack_b[i].append(el)

    for command in move_input:
        (quantity, from_index, to_index) = re.match(COMMAND_REGEXP, command).groups()

        move(stack_a, from_index, to_index, quantity)
        move(stack_b, from_index, to_index, quantity, True)

    print("".join([stack_a[i][0] for i in range(len(stack_a))]))
    print("".join([stack_b[i][0] for i in range(len(stack_b))]))



