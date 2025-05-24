import numpy as np
import matplotlib.pyplot as plt

# Constants
theta_E_GR = 3.2e-5  # Einstein radius in arcseconds for GR
alpha_values = [0.0, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2]  # Different α values for QIG

# Function to calculate the Einstein radius for QIG
def theta_E_QIG(alpha):
    return theta_E_GR * (1 + alpha)

# Generate positions for plotting
angles = np.linspace(0, 2 * np.pi, 100)

# Convert Einstein radii into Cartesian coordinates
def get_lensing_coordinates(theta_E):
    x = theta_E * np.cos(angles)
    y = theta_E * np.sin(angles)
    return x, y

# Plot the results
plt.figure(figsize=(6,6))

# Plot GR prediction as a thick, dashed red line
x_gr, y_gr = get_lensing_coordinates(theta_E_GR)
plt.plot(x_gr, y_gr, 'r--', linewidth=2.5, label="General Relativity (GR)")

# Plot QIG predictions for various α values
colors = ['b', 'orange', 'g', 'purple', 'brown', 'cyan', 'lime']
for alpha, color in zip(alpha_values, colors):
    x_qig, y_qig = get_lensing_coordinates(theta_E_QIG(alpha))
    plt.plot(x_qig, y_qig, color=color, linestyle='-', linewidth=1.5, label=f"QIG (α={alpha})")

# Add the lens position at the origin
plt.scatter(0, 0, color='black', s=50, label="Lens (Galaxy)")

# Labels and legend
plt.xlabel("X Position (arcseconds)")
plt.ylabel("Y Position (arcseconds)")
plt.title("Abell 1689 Lensing: GR vs QIG Model")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()