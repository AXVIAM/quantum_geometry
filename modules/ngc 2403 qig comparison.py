import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data_file = "ngc_2403_sparc_data.csv"
df = pd.read_csv(data_file)

# Extract data from the CSV
radius = df["Radius_kpc"].values
observed_velocity = df["Velocity_kms"].values  # Fixed column name
error = df["Error_kms"].values

# QIG Model Prediction (Modify as needed)
qig_velocity = observed_velocity * 0.9  # Placeholder for QIG calculation

# Save results to a text file
results_file = "ngc_2403_qig_comparison_results.txt"
with open(results_file, "w") as f:
    f.write("Radius (kpc), Observed Velocity (km/s), QIG Velocity (km/s), Difference (km/s)\n")
    for r, v_obs, v_qig in zip(radius, observed_velocity, qig_velocity):
        diff = v_qig - v_obs
        f.write(f"{r:.2f}, {v_obs:.2f}, {v_qig:.2f}, {diff:.2f}\n")

# Plot results
plt.figure(figsize=(8, 6))
plt.errorbar(radius, observed_velocity, yerr=error, fmt="ro", label="Observed Data (SPARC)")
plt.plot(radius, qig_velocity, "g-", label="QIG Predicted Curve")
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.title("NGC 2403: Observed vs. QIG Predicted Rotation Curve")
plt.legend()
plt.grid()
plt.savefig("ngc_2403_qig_comparison.png")
plt.show()

print(f"✅ Results saved to: {results_file}")
print(f"✅ Plot saved as: ngc_2403_qig_comparison.png")