import numpy as np
import matplotlib.pyplot as plt

# Define parameters
theta_E_GR = 1.5e-5  # Einstein radius for GR model (arcseconds)
alpha_values = [0.0, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2]  # QIG modification factors
lens_position = (0, 0)  # Assume centered lens

# Generate Einstein rings
fig, ax = plt.subplots(figsize=(6,6))
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'lime']

# Prepare results for saving
results_filename = "gravitational_lensing_results.txt"

with open(results_filename, "w") as file:
    file.write("Quantum Information Gravity - Gravitational Lensing Graph Results\n")
    file.write("------------------------------------------------------\n")
    file.write(f"GR Einstein Radius: {theta_E_GR:.6e} arcseconds\n")
    file.write("Modified Einstein Radii under QIG:\n")

    for alpha, color in zip(alpha_values, colors):
        theta_E_QIG = theta_E_GR * (1 + alpha)  # Modified Einstein radius
        file.write(f"  α = {alpha:.2f} → θ_E_QIG = {theta_E_QIG:.6e} arcseconds\n")
        circle = plt.Circle(lens_position, theta_E_QIG, color=color, fill=False, label=f"QIG (α={alpha})")
        ax.add_patch(circle)

# Plot GR reference
circle_GR = plt.Circle(lens_position, theta_E_GR, color='r', fill=False, linestyle='dashed', linewidth=2, label="General Relativity (GR)")
ax.add_patch(circle_GR)

# Format plot
ax.set_xlim(-4e-5, 4e-5)
ax.set_ylim(-4e-5, 4e-5)
ax.set_xlabel("X Position (arcseconds)")
ax.set_ylabel("Y Position (arcseconds)")
ax.set_title("Gravitational Lensing Graph: GR vs QIG Model")
ax.legend()
ax.set_aspect('equal')
plt.grid()

# Save image
image_filename = "gravitational_lensing_graph.png"
plt.savefig(image_filename, dpi=300)
plt.close()

print(f"✅ Script updated successfully.\nResults saved in {results_filename}\nImage saved as {image_filename}")
