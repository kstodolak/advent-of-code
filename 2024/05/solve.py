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

    good_order = []
    bad_idx = []
    for idx_update, _update in enumerate(updates):
      update = [int(x) for x in _update.split(',')]
      OK = True
      for idx,i in enumerate(update[1:], 1):
        if i in orders:
          i_should_be_before = orders[i]
          for j in update[:idx]:
            if j in i_should_be_before:
              bad_idx.append(idx_update)
              OK = False
              break
          if not OK:
            break
      if OK:
        good_order.append(update)

    part1 = 0
    for good in good_order:
      part1 += good[len(good)//2]

    print(part1)

    part2 = 0
    for b in bad_idx:
      update = [int(x) for x in updates[b].split(',')]
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
          else:
            corrected.append(i)

      part2 += corrected[len(corrected)//2]

    print(part2)


