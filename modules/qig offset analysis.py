import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the input data files for each galaxy
galaxies = {
    "NGC 3198": "ngc_3198_qig_comparison_results.txt",
    "NGC 2403": "ngc_2403_qig_comparison_results.txt",
    "UGC 128": "ugc_128_qig_comparison_results.txt"
}

# Initialize storage for the offset analysis
offset_data = {}

plt.figure(figsize=(10, 6))

# Determine the minimum length across all datasets to avoid indexing errors
min_length = min(len(pd.read_csv(galaxies["NGC 3198"], header=None)),
                 len(pd.read_csv(galaxies["NGC 2403"], header=None)),
                 len(pd.read_csv(galaxies["UGC 128"], header=None)))

# Process each galaxy
for galaxy, filename in galaxies.items():
    print(f"📂 Loading data for {galaxy} from {filename}")
    
    # Load the data without headers and manually assign column names
    data = pd.read_csv(filename, header=None, names=["Radius_kpc", "Observed_Velocity", "QIG_Velocity", "Difference"])
    print(f"✅ First 5 rows of {galaxy}:\n", data.head())
    
    # Trim data to the minimum length to avoid out-of-bounds errors
    data = data.iloc[:min_length]
    
    radius_kpc = data["Radius_kpc"].values  # Extract radius column
    observed_velocity = data["Observed_Velocity"].values  # Extract observed velocity
    qig_velocity = data["QIG_Velocity"].values  # Extract QIG predicted velocity
    
    # Compute velocity offset and percentage error
    velocity_offset = observed_velocity - qig_velocity
    percentage_offset = (velocity_offset / observed_velocity) * 100
    
    # Store in dictionary for further analysis
    offset_data[galaxy] = {
        "radius_kpc": radius_kpc,
        "velocity_offset": velocity_offset,
        "percentage_offset": percentage_offset
    }
    
    # Plot percentage offset vs. radius
    plt.plot(radius_kpc, percentage_offset, label=galaxy)

# Configure the plot
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.xlabel("Radius (kpc)")
plt.ylabel("Percentage Difference (%)")
plt.title("QIG vs. Observed Rotation Curve Offset Across Galaxies")
plt.legend()
plt.grid(True)
plt.savefig("qig_offset_analysis.png")
plt.show()

print("✅ Image analysis complete. Graph saved as: qig_offset_analysis.png")
