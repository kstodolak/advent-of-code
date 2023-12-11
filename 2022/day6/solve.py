#!/usr/local/bin/python3

def get_marker(input, marker_length):
    for i in range(0, len(input) - marker_length - 1, 1):
        marker = set(input[i:i+marker_length])
        if len(marker) == marker_length:
            return i + marker_length


with open('./input.txt') as f:
    data_stream = f.read()

    # Part 1
    print(get_marker(data_stream, 4))
    # Part 2
    print(get_marker(data_stream, 14))