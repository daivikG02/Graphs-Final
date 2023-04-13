import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Plot the graph
nx.draw(G, with_labels=True)
plt.show()
