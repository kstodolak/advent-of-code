#!/usr/local/bin/python3

variables = dict()
operations = {
    '-': lambda a,b: a - b,
    '+': lambda a,b: a + b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a / b
}


def get_value(name):
    var = variables[name].split(' ')

    if var[0].isnumeric():
        return int(var[0])
    else:
        a = get_value(var[0])
        b = get_value(var[2])
        return operations[var[1]](a, b)


with open('./input.txt') as f:
    lines = f.read().splitlines()

    for line in lines:
        (l, r) = line.split(':')
        variables[l.strip()] = r.strip()

    # part 1
    print(int(get_value('root')))

    # part 2
    (v1, _, v2) = variables['root'].split(' ')
    before = get_value(v1)
    variables['humn'] = str(int(variables['humn']) + 1)
    after = get_value(v1)
    rev = after > before
    (target_value, var) = (int(before), v2) if before == after else (int(get_value(v2)), v1)

    low = 0
    high = int(1e14)
    while low < high:
        mid = (low + high) // 2
        variables['humn'] = str(mid)
        result = get_value(var)
        if result == target_value:
            print(mid)
            break
        if rev:
            if result > target_value:
                high = mid
            else:
                low = mid
        else:
            if result > target_value:
                low = mid
            else:
                high = mid







