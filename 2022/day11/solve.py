#!/usr/local/bin/python3
import re
import collections


def parse_input(lines):
    monkeys_input = []
    cur_m = []
    for line in lines:
        if line == '':
            monkeys_input.append(cur_m)
            cur_m = []
        else:
            cur_m.append(line)
    monkeys_input.append(cur_m)
    return monkeys_input


with open('./input.txt') as f:
    lines = f.read().splitlines()
    monkeys_input = parse_input(lines)

    monkeys = collections.defaultdict(lambda: [])
    monkeys_rules = collections.defaultdict()
    monkeys_counters = collections.defaultdict()

    for i, monkey in enumerate(monkeys_input):
        (_, items, operation, test, test_pos, test_neg) = monkey
        items = re.findall(r'\d+', items)
        operation = operation[19:]
        test = re.findall(r'\d+', test)[0]
        test_pos = int(re.findall(r'\d+', test_pos)[0])
        test_neg = int(re.findall(r'\d+', test_neg)[0])

        monkeys_counters[i] = 0
        for item in items:
            monkeys[i].append(int(item))
            monkeys_rules[i] = (operation, test, test_pos, test_neg)

    for j in range(20):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            (operation, test, test_pos, test_neg) = monkeys_rules[i]
            while len(monkey) > 0:
                item = monkey.pop(0)
                monkeys_counters[i] += 1
                cur_operation = operation.replace('old', str(item))
                value = int(eval(cur_operation) / 3)
                if value % int(test) == 0:
                    monkeys[test_pos].append(value)
                else:
                    monkeys[test_neg].append(value)

    ls = list(monkeys_counters[i] for i in range(len(monkeys_counters)))
    ls.sort(reverse=True)
    print(ls[0] * ls[1])
