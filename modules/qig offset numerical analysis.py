import pandas as pd

# Define the input data files for each galaxy
galaxies = {
    "NGC 3198": "ngc_3198_qig_comparison_results.txt",
    "NGC 2403": "ngc_2403_qig_comparison_results.txt",
    "UGC 128": "ugc_128_qig_comparison_results.txt"
}

# Initialize storage for the offset analysis
offset_data = {}

# Process each galaxy
for galaxy, filename in galaxies.items():
    print(f"📂 Loading data for {galaxy} from {filename}")
    
    # Load the data without headers and manually assign column names
    data = pd.read_csv(filename, header=None, names=["Radius_kpc", "Observed_Velocity", "QIG_Velocity", "Difference"])
    print(f"✅ First 5 rows of {galaxy}:\n", data.head())
    
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

# Save numerical results
output_results = "qig_offset_analysis_results.txt"
print(f"📂 Attempting to save results to: {output_results}")  # Debugging print statement

try:
    with open(output_results, "w") as f:
        print("✅ File opened successfully for writing.")
        
        f.write("Radius (kpc), NGC 3198 Offset (%), NGC 2403 Offset (%), UGC 128 Offset (%)\n")
        f.write("=" * 75 + "\n")

        # Determine the minimum length across all datasets
        min_length = min(len(offset_data["NGC 3198"]["percentage_offset"]),
                         len(offset_data["NGC 2403"]["percentage_offset"]),
                         len(offset_data["UGC 128"]["percentage_offset"]))

        for i in range(min_length):
            radius = offset_data["NGC 3198"]["radius_kpc"][i]  # Use NGC 3198 as reference for radii
            offset_3198 = offset_data["NGC 3198"]["percentage_offset"][i]
            offset_2403 = offset_data["NGC 2403"]["percentage_offset"][i]
            offset_128 = offset_data["UGC 128"]["percentage_offset"][i]

            f.write(f"{radius:.2f}, {offset_3198:.2f}, {offset_2403:.2f}, {offset_128:.2f}\n")

        print("✅ File write successful.")

    print(f"✅ File successfully saved: {output_results}")

except Exception as e:
    print(f"❌ ERROR: Could not save file! Reason: {e}")
