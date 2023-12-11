#!/usr/local/bin/python3
from cycledlist import CycledList


def go_right(node, repeats):
    current = node
    for i in range(repeats):
        current = current.next

    return current


def go_left(node, repeats):
    current = node
    for i in range(repeats):
        current = current.prev

    return current


def mix(numbers, sequence):
    for i in range(len(numbers)):
        node = numbers[i]
        current = node
        left = True if node.value < 0 else False
        nn = abs(node.value) % (len(numbers) - 1) if abs(node.value) > len(numbers) else abs(node.value)
        if nn == 0:
            continue
        if left:
            new_current = go_left(current, nn)
            new_node = sequence.put_before(new_current, node.value)
        else:
            new_current = go_right(current, nn)
            new_node = sequence.put_after(new_current, node.value)

        sequence.delete(current)
        numbers[i] = new_node


with open('./input.txt') as f:
    numbers = list(map(int, f.read().splitlines()))

    sequence = CycledList()
    sequence.from_array(numbers.copy())

    # part 1
    mix(sequence.to_nodes_array(), sequence)
    seq_arr = sequence.to_array()
    zero = seq_arr.index(0)
    result = sum([
        seq_arr[(zero + 1000) % len(seq_arr)],
        seq_arr[(zero + 2000) % len(seq_arr)],
        seq_arr[(zero + 3000) % len(seq_arr)]
    ])
    print(result)

    # part 2
    sequence_2 = CycledList()
    numbers_with_key = list(map(lambda x: x * 811589153, numbers.copy()))
    sequence_2.from_array(numbers_with_key)
    sequence_nodes = sequence_2.to_nodes_array()
    for _ in range(10):
        mix(sequence_nodes, sequence_2)
    seq_arr_2 = sequence_2.to_array()
    zero = seq_arr_2.index(0)
    result = sum([
        seq_arr_2[(zero + 1000) % len(seq_arr_2)],
        seq_arr_2[(zero + 2000) % len(seq_arr_2)],
        seq_arr_2[(zero + 3000) % len(seq_arr_2)]
    ])
    print(result)
