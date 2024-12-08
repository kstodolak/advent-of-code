import os

with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    data = f.read().strip()
    rules, updates = (x.splitlines() for x in data.split('\n\n'))
    orders = {}

    for rule in rules:
      a, b = (int(x) for x in rule.split('|'))
      if a not in orders:
        orders[a] = set()
      orders[a].add(b)

    part1 = 0
    part2 = 0
    for _update in updates:
      update = [int(x) for x in _update.split(',')]
      OK = True
      corrected = [update[0]]
      for idx, i in enumerate(update[1:], 1):
        if i not in orders:
          corrected.append(i)
        else:
          i_should_be_before = orders[i]
          already_in_idx = []
          for ii in i_should_be_before:
            if ii in corrected:
              already_in_idx.append(corrected.index(ii))
          if len(already_in_idx) > 0:
            corrected.insert(min(already_in_idx), i)
            OK = False
          else:
            corrected.append(i)
      if OK:
        part1 += corrected[len(corrected)//2]
      else:
        part2 += corrected[len(corrected)//2]

    print(part1)
    print(part2)


