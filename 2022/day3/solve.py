#!/usr/local/bin/python3

# Score system:
# a - z = 1 - 26
# A - Z = 27 - 52

def get_number_score(chars_set):
    score = 0
    for char in chars_set:
        if char.islower():
            score += ord(char) - 96
        else:
            score += ord(char) - 38
    return score


with open('./input.txt') as f:
    lines = f.read().splitlines()

    # part 1
    score_1 = 0
    for line in lines:
        mid_point = len(line) // 2
        part_1 = set(line[:mid_point])
        part_2 = set(line[mid_point:])

        duplicates = set(part_1 & part_2)
        score_1 += get_number_score(duplicates)

    # part 2
    lines_grouped = []
    for i in range(0, len(lines), 3):
        lines_grouped.append(lines[i:i+3])

    score_2 = 0
    for line in lines_grouped:
        (l1, l2, l3) = line
        duplicates = set(set(l1) & set(l2) & set(l3))
        score_2 += get_number_score(duplicates)

    print(score_1)
    print(score_2)
