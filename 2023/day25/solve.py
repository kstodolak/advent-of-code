import os
import networkx as nx

with open(os.path.dirname(__file__) + "/input.txt") as f:
  lines = f.read().splitlines()
  modules = dict()

  for line in lines:
    module, rest = line.split(":")
    connected_to = rest[1:].split(" ")
    modules[module] = connected_to

  G = nx.Graph()
  for module, connected_to in modules.items():
    for n in connected_to:
      G.add_edge(module, n)

  minimum_cuts = nx.minimum_edge_cut(G)
  assert len(minimum_cuts) == 3
  G.remove_edges_from(minimum_cuts)

  graphs = list(nx.connected_components(G))
  assert len(graphs) == 2
  print(len(graphs[0]) * len(graphs[1]))
