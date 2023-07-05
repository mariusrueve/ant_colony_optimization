import networkx as nx
import numpy as np
import string

dt = [("len", float)]

distances = np.array(
    [
        [np.inf, 2, 2, 5, 7],
        [2, np.inf, 4, 8, 2],
        [2, 4, np.inf, 1, 3],
        [5, 8, 1, np.inf, 2],
        [7, 2, 3, 2, np.inf],
    ]
)
distances = distances.view(dt)

G = nx.Graph(distances)

G = nx.drawing.nx_agraph.to_agraph(G)

# Add edge labels with the path lengths to the graph
for edge in G.edges():
    print(edge[0], edge[1])
    edge.attr["label"] = edge.attr["len"]

shortest_path = [(0, 2), (2, 3), (3, 4), (4, 1), (1, 0)]
# make the edges that form the shortest path red
# for edge in shortest_path:
#     G.get_edge(edge[0], edge[1]).attr["color"] = "red"
#     G.get_edge(edge[0], edge[1]).attr["penwidth"] = "3.0"
#     # also make the labels red
#     G.get_edge(edge[0], edge[1]).attr["fontcolor"] = "red"

G.node_attr.update(
    color="lightblue",
    style="filled",
)
G.edge_attr.update(color="black", width="2.0")

G.draw("out-1.png", format="png", prog="neato")
