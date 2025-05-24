import numpy as np
import matplotlib.pyplot as plt

# Define parameters
r_range = np.linspace(1, 30, 100)  # Radius range (in kpc)
G = 4.30091e-6  # Gravitational constant in kpc⋅(km/s)^2⋅M☉^−1
M = 1e11  # Mass of galaxy in solar masses
alpha = 0.1  # Scaling parameter for QIG

# Compute velocities
v_newtonian = np.sqrt(G * M / r_range)  # Standard Newtonian model
v_gr = v_newtonian * (1 + 0.05 * np.exp(-r_range / 10))  # General Relativity corrections
I_r = np.log(1 + r_range)  # QIG information density function (placeholder)
v_qig = np.sqrt(G * M / r_range + alpha * np.gradient(I_r, r_range))  # QIG-modified velocity

# Generate plot comparing GR and QIG
plt.figure(figsize=(8, 6))
plt.plot(r_range, v_newtonian, 'b--', linewidth=2.5, label="Newtonian Gravity")
plt.plot(r_range, v_gr, 'orange', linestyle='dotted', linewidth=2, label="General Relativity")
plt.plot(r_range, v_qig, 'g-', linewidth=2, label="Quantum Information Gravity")

# Labels and formatting
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.title("GR vs QIG: Comparison of Rotation Curves")
plt.legend()
plt.grid(True)

# Save the figure
image_filename = "gr_vs_qig_comparison.png"
plt.savefig(image_filename, dpi=300)
plt.close()

# Save numerical results to a log file
results_filename = "gr_vs_qig_comparison_results.txt"
with open(results_filename, "w") as file:
    file.write("Quantum Information Gravity - GR vs QIG Comparison Results\n")
    file.write("------------------------------------------------------\n")
    file.write("Radius (kpc) | Newtonian Velocity (km/s) | GR Velocity (km/s) | QIG Velocity (km/s)\n")

    for i in range(len(r_range)):
        file.write(f"{r_range[i]:.2f} kpc | {v_newtonian[i]:.2f} km/s | {v_gr[i]:.2f} km/s | {v_qig[i]:.2f} km/s\n")

print(f"✅ Script updated successfully.\nResults saved in {results_filename}\nImage saved as {image_filename}")
