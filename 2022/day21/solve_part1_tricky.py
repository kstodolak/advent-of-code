with open('./input.txt') as f:
    lines = list(map(lambda x: x.replace(':', '='), f.read().splitlines()))
    i = 0
    variables = dict()
    while len(lines) > 0:
        line = lines[i]
        try:
            exec(line)
            lines.pop(i)
            i = 0
        except NameError:
            i += 1

    print(int(root))