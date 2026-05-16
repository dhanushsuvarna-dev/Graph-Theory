import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

edge_list = [(2, 4), (2, 6), (3, 6), (4, 6), (3, 5), (4, 3), (5, 6)]

G = nx.Graph()
G = nx.from_edgelist(edge_list)

print(dict(G.degree)[2])

nx.draw_spring(G, with_labels=True)
plt.show()

nx.draw_planar(G, with_labels=True)
plt.show()
