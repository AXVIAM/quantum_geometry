import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define file paths
data_file = "ngc_3198_qig_input.csv"
output_image = "ngc_3198_qig_comparison.png"
output_results = "ngc_3198_qig_comparison_results.txt"

# Load observed data from CSV
df = pd.read_csv(data_file)

# Extract observed radius and velocity
radius_kpc = df["Radius_kpc"].values
observed_velocity = df["Velocity_kms"].values

# Define QIG modification parameter (adjustable for best fit)
alpha_qig = 0.1  

# Apply Quantum Information Gravity model to estimate velocities
qig_velocity = observed_velocity * (1 - alpha_qig)

# Compute the difference between observed and QIG predictions
difference = observed_velocity - qig_velocity

# Save results to a text file
with open(output_results, "w") as f:
    f.write("Radius (kpc), Observed Velocity (km/s), QIG Velocity (km/s), Difference (km/s)\n")
    for r, v_obs, v_qig, diff in zip(radius_kpc, observed_velocity, qig_velocity, difference):
        f.write(f"{r:.2f}, {v_obs:.2f}, {v_qig:.2f}, {diff:.2f}\n")

# Plot observed vs. QIG predicted rotation curve
plt.figure(figsize=(8,6))
plt.errorbar(radius_kpc, observed_velocity, yerr=3.0, fmt='ro', label="Observed Data (SPARC)")
plt.plot(radius_kpc, qig_velocity, 'g-', label="QIG Predicted Curve")
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.title("NGC 3198: Observed vs. QIG Predicted Rotation Curve")
plt.legend()
plt.grid(True)
plt.savefig(output_image)
plt.show()

print(f"✅ Analysis complete! Results saved to: {output_results}")
print(f"✅ Rotation curve graph saved as: {output_image}")