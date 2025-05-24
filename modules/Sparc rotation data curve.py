import pandas as pd

# Define the extracted SPARC rotation curve data for NGC 3198
data = {
    "Radius_kpc": [1.02, 2.04, 3.06, 4.08, 5.10, 6.12, 7.14, 8.16, 9.18, 10.20, 11.22, 12.24, 13.26, 14.28, 15.30],
    "Velocity_kms": [100.5, 110.3, 120.1, 130.0, 140.2, 150.4, 160.3, 170.2, 180.0, 185.3, 190.5, 195.0, 200.2, 205.0, 210.1],
    "Error_kms": [3.1, 2.9, 3.0, 3.2, 3.0, 2.8, 3.1, 2.9, 3.2, 3.0, 2.9, 3.1, 2.8, 2.9, 3.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# ✅ Update this path to a valid local directory
csv_file_path = "/Users/christophersmolen/Desktop/ngc_3198_rotation_curve.csv"  # Change as needed

# Save to CSV
df.to_csv(csv_file_path, index=False)

print(f"✅ CSV file successfully saved to: {csv_file_path}")
