import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ✅ Ensure the script looks for the correct file path
data_file = "/Users/christophersmolen/Desktop/QuantumInformationGravity/ngc_3198_sparc_data.csv"

# Load SPARC data for NGC 3198
try:
    data = pd.read_csv(data_file)
    print("✅ Successfully loaded NGC 3198 rotation curve data.")
except FileNotFoundError:
    print(f"❌ Error: File not found at {data_file}. Please verify the file exists.")
    exit()

# Extract relevant data
r_obs = data["Radius_kpc"].values  # Radius in kpc
v_obs = data["Velocity_kms"].values  # Observed velocity in km/s
v_err = data["Error_kms"].values  # Measurement errors

# Define QIG Model Predictions
G = 4.30091e-6  # Gravitational constant in kpc⋅(km/s)^2⋅M☉^−1
M = 1e11  # Estimated galaxy mass in solar masses
alpha = 0.1  # QIG scaling parameter

# Compute QIG velocities
I_r = np.log(1 + r_obs)  # Placeholder for information-density function
v_qig = np.sqrt(G * M / r_obs + alpha * np.gradient(I_r, r_obs))

# Generate plot comparing observed vs. QIG model
plt.figure(figsize=(8, 6))
plt.errorbar(r_obs, v_obs, yerr=v_err, fmt='ro', label="Observed Data (SPARC)")
plt.plot(r_obs, v_qig, 'g-', linewidth=2, label="QIG Predicted Curve")

# Labels and formatting
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.title("NGC 3198: Observed vs. QIG Predicted Rotation Curve")
plt.legend()
plt.grid(True)

# Save the figure
image_filename = "ngc_3198_rotation_comparison.png"
plt.savefig(image_filename, dpi=300)
plt.close()

# Save numerical results to a log file
results_filename = "ngc_3198_rotation_comparison_results.txt"
with open(results_filename, "w") as file:
    file.write("Quantum Information Gravity - NGC 3198 Rotation Curve Comparison\n")
    file.write("------------------------------------------------------\n")
    file.write("Radius (kpc) | Observed Velocity (km/s) | QIG Velocity (km/s)\n")

    for i in range(len(r_obs)):
        file.write(f"{r_obs[i]:.2f} kpc | {v_obs[i]:.2f} km/s | {v_qig[i]:.2f} km/s\n")

print(f"✅ Script executed successfully.\nResults saved in {results_filename}\nImage saved as {image_filename}")
