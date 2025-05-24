import numpy as np
import matplotlib.pyplot as plt

# Define angle range in arcseconds
theta = np.linspace(0.5, 10, 100)

# Define GR deflection angle (baseline model)
deflection_gr = 4 * 6.67430e-11 * 1e30 / (3e8**2 * theta)

# Define QIG modifications with different α values
alpha_values = [0.0, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2]
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']

plt.figure(figsize=(8,6))

# Plot GR as a clear reference in **red dashed line**
plt.plot(theta, deflection_gr, 'r--', linewidth=2.5, label="General Relativity (GR)")

# Plot Quantum Information Gravity variations
for alpha, color in zip(alpha_values, colors):
    deflection_qig = deflection_gr * (1 + alpha)  # Adjusted model
    plt.plot(theta, deflection_qig, color=color, linewidth=2, label=f"QIG (α={alpha})")

plt.xlabel("Angle (arcseconds)")
plt.ylabel("Deflection Angle (radians)")
plt.title("Gravitational Lensing: GR vs. Quantum Information Gravity")
plt.legend()
plt.grid()
plt.show()