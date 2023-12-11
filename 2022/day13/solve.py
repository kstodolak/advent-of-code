#!/usr/local/bin/python3
from copy import deepcopy
from functools import cmp_to_key


def check_order(q_a, q_b):
    q_a  = deepcopy(q_a)
    q_b = deepcopy(q_b)
    while len(q_a) > 0 and len(q_b) > 0:
        a = q_a.pop(0)
        b = q_b.pop(0)
        if type(a) is int and type(b) is int:
            if a > b:
                return -1
            if a < b:
                return 1
            continue
        aa = [a] if type(a) is int else a
        bb = [b] if type(b) is int else b

        check = check_order(aa, bb)
        if check == 0:
            continue

        return check

    if len(q_a) == 0 and len(q_b) == 0:
        return 0
    if len(q_a) == 0:
        return 1

    return -1


with open('./input.txt') as f:
    file = list(map(lambda x: x.splitlines(), f.read().split('\n\n')))

    pairs = []
    packets = []
    for i, pair in enumerate(file, 1):
        (a, b) = pair
        q_a = list(eval(a))
        q_b = list(eval(b))
        pairs.append((q_a, q_b))
        packets.extend([q_a, q_b])

    pairs_2 = deepcopy(pairs)
    right_order = []
    for i, (a, b) in enumerate(pairs, 1):
        if check_order(a, b) == 1:
            right_order.append(i)

    # part 1
    print(sum(right_order))

    divider_packets = [[[2]], [[6]]]
    packets.extend(divider_packets)

    packets.sort(key=cmp_to_key(check_order), reverse=True)

    # part 2
    i1 = packets.index(divider_packets[0]) + 1
    i2 = packets.index(divider_packets[1]) + 1
    print(i1 * i2)



