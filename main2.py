import squarify
import matplotlib.pyplot as plt

# Define the sizes of the rectangles
sizes = [100, 50, 25, 10, 5]

# Define the labels for the rectangles
labels = ["A", "B", "C", "D", "E"]

# Create the treemap
squarify.plot(sizes=sizes, label=labels, alpha=.7)

# Show the treemap
plt.axis('off')
plt.show()
