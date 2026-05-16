import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(2, 2), (3, 3), (4, 4), (6, 6), (2, 4), (2, 6), (3, 6), ]
node_list = ["A", "B", "C", "D"]

G = nx.from_edgelist(edge_list)


nx.draw_spring(G, with_labels=True)
plt.show()
