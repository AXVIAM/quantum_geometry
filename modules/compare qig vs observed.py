import numpy as np
import pandas as pd

# Define file paths
observed_data_file = "/Users/christophersmolen/Desktop/QuantumInformationGravity/ngc_3198_sparc_data.csv"
qig_results_file = "/Users/christophersmolen/Desktop/QuantumInformationGravity/ngc_3198_rotation_comparison_results.txt"

# Load observed data
try:
    observed_data = pd.read_csv(observed_data_file)
    print("✅ Successfully loaded observed galaxy rotation data.")
except FileNotFoundError:
    print(f"❌ Error: Observed data file not found at {observed_data_file}.")
    exit()

# Extract relevant columns
r_obs = observed_data["Radius_kpc"].values
v_obs = observed_data["Velocity_kms"].values

# Load QIG results
qig_data = []
try:
    with open(qig_results_file, "r") as file:
        lines = file.readlines()[3:]  # Skip header lines
        for line in lines:
            parts = line.strip().split("|")
            if len(parts) == 3:
                radius, obs_vel, qig_vel = map(str.strip, parts)
                qig_data.append((float(radius.split()[0]), float(qig_vel.split()[0])))
    print("✅ Successfully loaded QIG results.")
except FileNotFoundError:
    print(f"❌ Error: QIG results file not found at {qig_results_file}.")
    exit()

# Convert QIG data to numpy arrays
r_qig, v_qig = zip(*qig_data)
r_qig = np.array(r_qig)
v_qig = np.array(v_qig)

# Compute differences
absolute_diff = np.abs(v_obs - v_qig)
percentage_diff = (absolute_diff / v_obs) * 100

# Save results
comparison_file = "/Users/christophersmolen/Desktop/QuantumInformationGravity/ngc_3198_qig_vs_observed_comparison.txt"

with open(comparison_file, "w") as file:
    file.write("QIG vs Observed Rotation Curve Comparison for NGC 3198\n")
    file.write("------------------------------------------------------\n")
    file.write("Radius (kpc) | Observed Velocity (km/s) | QIG Velocity (km/s) | Absolute Difference | % Difference\n")
    
    for i in range(len(r_obs)):
        flag = "❗" if percentage_diff[i] > 10 else ""  # Flag large deviations
        file.write(f"{r_obs[i]:.2f} kpc | {v_obs[i]:.2f} km/s | {v_qig[i]:.2f} km/s | {absolute_diff[i]:.2f} km/s | {percentage_diff[i]:.2f}% {flag}\n")

print(f"✅ Comparison completed. Results saved in {comparison_file}")
