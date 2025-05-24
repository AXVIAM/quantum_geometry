import numpy as np
import matplotlib.pyplot as plt

# QIR Scaling Model Using Decompression-First Approach
C = np.pi  # Pi as a fundamental scaling constant

# Define the decompression-first scaling function
def decompression_first_scaling(mass, distance, information_density):
    # Decompression: Information expands first
    decompressed_value = np.exp(mass * distance / (1 + information_density)) - 1
    # Compression: Information is structured back into measurable physics
    structured_value = np.log(1 + decompressed_value)
    return C * structured_value

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Black hole entropy, lensing, and quantum uncertainty data
    observed_masses = np.array([10, 12, 15])  # Replace with actual dataset values
    observed_distances = np.array([110, 95, 130])  # Replace with actual dataset values
    observed_information_density = np.array([0.04, 0.05, 0.06])  # Replace with actual dataset values
    observed_values = np.array([100.5, 144.0, 225.5])  # Replace with real observed values
    
    predicted_values = [decompression_first_scaling(m, d, I) for m, d, I in zip(observed_masses, observed_distances, observed_information_density)]
    
    # Save results to TXT file
    with open("output_decompress_first_test.txt", "w") as file:
        file.write("Observed Data vs. QIR Predictions (With Decompression-First Scaling)\n")
        file.write("Mass (Solar Masses) | Distance (Units) | Information Density | Observed Value | QIR-Predicted Value (Corrected)\n")
        for m, d, I, ov, pv in zip(observed_masses, observed_distances, observed_information_density, observed_values, predicted_values):
            file.write(f"{m:.2f} | {d:.2f} | {I:.4f} | {ov:.4f} | {pv:.4f}\n")

    # Plot real vs. simulated data
    plt.scatter(observed_distances, observed_values, color='red', label="Observed Data")
    plt.scatter(observed_distances, predicted_values, color='blue', label="QIR-Predicted Values (Decompression-First)")
    plt.xlabel("Distance")
    plt.ylabel("Effect Magnitude")
    plt.title("QIR Predictions vs. Observed Data (Decompression-First Model)")
    plt.legend()
    plt.savefig("output_decompress_first_test.png")

    print("Results saved as 'output_decompress_first_test.txt' and 'output_decompress_first_test.png'")
else:
    mass = 10  # Solar masses
    distance = 100  # Arbitrary units
    information_density = 0.05  # QIR correction term
    print(f"Decompression-First Effect: {decompression_first_scaling(mass, distance, information_density)}")
