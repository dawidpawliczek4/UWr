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
def plot_polynomial(n_values, type="Equidistant"):
    x = np.linspace(-1, 1, 500)
    plt.figure(figsize=(12, 8))
    
    for n in n_values:
        nodes = generate_nodes(n, type=type)
        y = compute_polynomial(x, nodes)
        plt.plot(x, y, label=f"n={n}")
        plt.ylim(-0.5, 0.5)  # Adjust the y-axis limits to show a bigger picture of the function
        y = compute_polynomial(x, nodes)
        plt.plot(x, y, label=f"n={n}")
        
    plt.title(f"Polynomials for {type} Nodes")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# array from 4 to 20
n_values = np.arange(4, 21)

# Plot for equidistant nodes
plot_polynomial(n_values, type="Equidistant")

# Plot for Chebyshev nodes
plot_polynomial(n_values, type="Chebyshev")
