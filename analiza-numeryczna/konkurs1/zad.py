import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from matplotlib.collections import LineCollection

def create_spline_curve(points, num_interpolated_points=1000):
    """Create a smooth spline curve from a set of points."""
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    # Create parameter t for interpolation
    t = np.zeros(len(points))
    for i in range(1, len(points)):
        t[i] = t[i-1] + np.sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)
    
    # Normalize t to [0, 1]
    if t[-1] != 0:
        t = t/t[-1]
    
    # Create interpolation
    cs_x = CubicSpline(t, x)
    cs_y = CubicSpline(t, y)
    
    # Generate smooth curve
    t_new = np.linspace(0, 1, num_interpolated_points)
    return cs_x(t_new), cs_y(t_new)

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Define points for "PWO"
pwo_points = [
    # 'P'
[(57.80645161290323, 125.62162117452436),
(52.301075268817215, 44.734937965260485)]

]

# Define points for "+"
plus_points = [
    [(12.5, 3), (12.5, 2)],  # vertical line
    [(12, 2.5), (13, 2.5)]   # horizontal line
]

# Define points for smile
smile_points = [
    [(20, 2), (21, 2.5), (22, 2)]
]

# Colors for different parts
colors = ['red'] * len(pwo_points + plus_points + smile_points)

# Plot each letter/symbol
all_segments = []
for points in (pwo_points + plus_points + smile_points):
    x, y = create_spline_curve(points)
    all_segments.append(np.column_stack((x, y)))

# Create line collection
lc = LineCollection(all_segments, colors=colors, linewidth=2)
ax.add_collection(lc)

# Set plot limits and aspect ratio
ax.set_xlim(0, 25)
ax.set_ylim(0, 6)
ax.set_aspect('equal')

# Remove axes
ax.axis('off')

plt.show()