#!/usr/local/bin/python3

with open('./input.txt') as f:
    lines = f.read().splitlines()

    calories = []
    elfSum = 0

    for line in lines:
        if line == "":
            calories.append(elfSum)
            elfSum = 0
        else:
            elfSum += int(line)

    calories.sort(reverse=True)

    # part 1
    print(calories[0])

    # part 2
    print(sum(calories[:3]))
