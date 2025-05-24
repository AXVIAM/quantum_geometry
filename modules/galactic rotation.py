import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 4.30091e-6  # Gravitational constant in kpc⋅(km/s)^2⋅M☉^−1
M = 1e11  # Mass of galaxy in solar masses
alpha = 0.1  # Scaling parameter for QIG

# Define radius range (in kpc)
r_range = np.linspace(1, 30, 100)

# Newtonian Gravity Model (No Dark Matter)
v_n = np.sqrt(G * M / r_range)

# General Relativity Correction (Placeholder approximation)
v_gr = v_n * (1 + 0.05 * np.exp(-r_range / 10))  # Small relativistic correction

# Quantum Information Gravity Model (Structured Information Effect)
I_r = np.log(1 + r_range)  # Placeholder for information-density function
v_qig = np.sqrt(G * M / r_range + alpha * np.gradient(I_r, r_range))

# Ensure visibility of all curves
plt.figure(figsize=(8, 6))

plt.plot(r_range, v_n, 'b--', label="Newtonian Gravity", linewidth=3.0, zorder=3)
plt.plot(r_range, v_gr, 'orange', linestyle='dotted', label="General Relativity", linewidth=2.0, zorder=2)
plt.plot(r_range, v_qig, 'g-', label="Quantum Information Gravity", linewidth=2.0, zorder=1)

# Add observed data points (Placeholder for real data)
obs_r = np.array([5, 10, 15, 20])
obs_v = np.array([180, 160, 150, 145])
plt.scatter(obs_r, obs_v, color='red', label="Observed Data", zorder=4)

# Labels and title
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.title("Galactic Rotation Curves: Newtonian vs GR vs QIG")
plt.legend()
plt.grid(True)

# Save the figure
image_filename = "galactic_rotation.png"
plt.savefig(image_filename, dpi=300)
plt.close()

# Save numerical results to a log file
results_filename = "galactic_rotation_results.txt"
with open(results_filename, "w") as file:
    file.write("Quantum Information Gravity - Galactic Rotation Results\n")
    file.write("------------------------------------------------------\n")
    file.write("Radius (kpc) | Newtonian Velocity (km/s) | GR Velocity (km/s) | QIG Velocity (km/s)\n")

    for i in range(len(r_range)):
        file.write(f"{r_range[i]:.2f} kpc | {v_n[i]:.2f} km/s | {v_gr[i]:.2f} km/s | {v_qig[i]:.2f} km/s\n")

print(f"✅ Script updated successfully.\nResults saved in {results_filename}\nImage saved as {image_filename}")
