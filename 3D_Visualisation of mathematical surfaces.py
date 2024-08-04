import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the mathematical functions to visualize
def sphere(x, y, z):
    return x**2 + y**2 + z**2

def saddle(x, y, z):
    return x**2 - y**2 - z**2

def torus(x, y, z):
    R = 1  # Major radius
    r = 0.3  # Minor radius
    return (R - np.sqrt(x**2 + y**2))**2 + z**2 - r**2

# Generate data points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
z = np.linspace(-2, 2, 100)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')  # Use indexing='ij' to ensure Z is 2D

# Evaluate the chosen mathematical function at each point
# Example usage: Z = sphere(X, Y, Z)
Z = saddle(X, Y, Z)

# Create 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X[:,:,0], Y[:,:,0], Z[:,:,0], cmap='viridis')  # Plot one 2D slice of Z

# Customize plot appearance
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Saddle Surface')

plt.show()
