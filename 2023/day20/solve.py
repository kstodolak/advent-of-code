#!/usr/bin/python3
import os
import math

modules = dict()
out_pulses = []
crucial_modules = None
cycles = []

class Module:
  memory = None
  def __init__(self, name:str, destinations:list):
    self.destinations = destinations
    self.state = False
    if name == 'broadcaster':
      self.type = 'B'
      self.name = name
    elif name in ['button', 'output', 'rx']:
      self.name = name
      self.type = name
    elif name.startswith('%'):
      self.type = 'F'
      self.name = name[1:]
    elif name.startswith('&'):
      self.type = 'C'
      self.name = name[1:]
      self.memory = dict()
  
  def get_signal(self, sent_from, i):
    signal = modules[sent_from].state
    out_pulses.append(signal)

    if self.type == 'B':
      self.state = signal
      return [(self.name, d) for d in self.destinations]
    
    if self.type == 'F':
      if not signal: 
        self.state = not self.state  
        return [(self.name, d) for d in self.destinations]


    if self.type == 'C':
      self.memory[sent_from] = signal
      self.state = not all(x for x in self.memory.values())
      if self.name in crucial_modules and self.state:
        cycles.append(i)
      return [(self.name, d) for d in self.destinations]

def click(i):
  todo = [('button', 'broadcaster')]

  while todo:
    sent_from, name = todo.pop(0)
    M = modules[name]
    to_extend = M.get_signal(sent_from, i)
    if to_extend is None: continue
    for e in to_extend:
      todo.append(e)
  

with open(os.path.dirname(__file__) + '/input.txt') as f:
  lines = f.read().splitlines()

  modules['button'] = Module('button', ['broadcaster'])
  modules['output'] = Module('output', [])
  modules['rx'] = Module('rx', [])
  for line in lines:
    (name, destinations) = line.split(' -> ')
    destinations = destinations.split(', ')
    M = Module(name, destinations)
    name = name if name == 'broadcaster' else name[1:]
    modules[name] = M
  
  connected_to_rx = None
  for name, module in modules.items():
    for d in module.destinations:
      if d == 'rx': connected_to_rx = name
      if modules[d].type == 'C':
        modules[d].memory[name] = False

  crucial_modules = modules[connected_to_rx].memory.keys()
  
  i = 1
  while len(cycles) < len(crucial_modules):
    click(i)
    if i == 1000:
      # part 1
      print(out_pulses.count(False) * out_pulses.count(True))
    i += 1

  # part2
  print(math.lcm(*cycles))