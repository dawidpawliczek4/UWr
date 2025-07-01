import numpy as np
import matplotlib.pyplot as plt

# Function to compute Pn+1(x) for given x and nodes
def compute_polynomial(x, nodes):
    p = 1
    for node in nodes:
        p *= (x - node)
    return p

# Generate equidistant nodes and Chebyshev nodes in [-1, 1]
def generate_nodes(n, type="Equidistant"):
    if type == "Equidistant":
        return np.linspace(-1, 1, n+1)
    elif type == "Chebyshev":
        return np.array([np.cos((2*k + 1) * np.pi / (2 * (n + 1))) for k in range(n+1)])

# Plotting function
def plot_polynomial(ax, n_values, type="Equidistant"):
    x = np.linspace(-1, 1, 500)
    for n in n_values:
        nodes = generate_nodes(n, type=type)
        y = compute_polynomial(x, nodes)
        ax.plot(x, y, label=f"n={n}")
    ax.set_title(f"Polynomials for {type} Nodes")
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")
    ax.legend()
    ax.grid(True)
    ax.set_xlim(-1, 1)  # Fix x-axis range
    ax.set_ylim(-0.2, 0.2)  # Fix y-axis range

# Define n values
n_values = np.arange(4, 21)

# Create two subplots: one for equidistant nodes and one for Chebyshev nodes
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot for equidistant nodes
plot_polynomial(axs[0], n_values, type="Equidistant")

# Plot for Chebyshev nodes
plot_polynomial(axs[1], n_values, type="Chebyshev")

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
