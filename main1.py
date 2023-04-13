import seaborn as sns
import numpy as np

# Create a random matrix
matrix = np.random.rand(10, 10)

# Create a heatmap of the matrix
sns.heatmap(matrix, cmap="YlGnBu")
