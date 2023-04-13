import plotly.graph_objects as go

# Define the nodes and links for the Sankey diagram
nodes = ["Node A", "Node B", "Node C", "Node D", "Node E"]
links = dict(source=[0, 1, 1, 2, 2, 3], target=[2, 3, 4, 3, 4, 4], value=[8, 4, 2, 6, 4, 2])

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(node=dict(label=nodes[i]), link=dict(source=links['source'][i], target=links['target'][i], value=links['value'][i])) for i in range(len(links['source']))])

# Show the Sankey diagram
fig.show()
