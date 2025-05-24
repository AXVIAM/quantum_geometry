import numpy as np
import matplotlib.pyplot as plt

# QIR Scaling Model Using Entropy-Constrained Information Release
C = np.pi  # Pi remains fundamental unless proven otherwise

# Define the entropy-limited decompression function
def entropy_constrained_scaling(mass, distance, information_density):
    # Decompression: Information expands but is constrained by entropy limits
    decompressed_value = np.exp(mass * distance / (1 + information_density)) - 1
    # Apply entropy-based release function to regulate expansion
    entropy_limited_value = decompressed_value / (1 + np.log(1 + decompressed_value))
    return C * entropy_limited_value

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Black hole entropy, lensing, and quantum uncertainty data
    observed_masses = np.array([10, 12, 15])  # Replace with actual dataset values
    observed_distances = np.array([110, 95, 130])  # Replace with actual dataset values
    observed_information_density = np.array([0.04, 0.05, 0.06])  # Replace with actual dataset values
    observed_values = np.array([100.5, 144.0, 225.5])  # Replace with real observed values
    
    predicted_values = [entropy_constrained_scaling(m, d, I) for m, d, I in zip(observed_masses, observed_distances, observed_information_density)]
    
    # Save results to TXT file
    with open("output_entropy_constrained_test.txt", "w") as file:
        file.write("Observed Data vs. QIR Predictions (With Entropy-Constrained Scaling)\n")
        file.write("Mass (Solar Masses) | Distance (Units) | Information Density | Observed Value | QIR-Predicted Value (Corrected)\n")
        for m, d, I, ov, pv in zip(observed_masses, observed_distances, observed_information_density, observed_values, predicted_values):
            file.write(f"{m:.2f} | {d:.2f} | {I:.4f} | {ov:.4f} | {pv:.4f}\n")

    # Plot real vs. simulated data
    plt.scatter(observed_distances, observed_values, color='red', label="Observed Data")
    plt.scatter(observed_distances, predicted_values, color='blue', label="QIR-Predicted Values (Entropy-Constrained)")
    plt.xlabel("Distance")
    plt.ylabel("Effect Magnitude")
    plt.title("QIR Predictions vs. Observed Data (Entropy-Constrained Model)")
    plt.legend()
    plt.savefig("output_entropy_constrained_test.png")

    print("Results saved as 'output_entropy_constrained_test.txt' and 'output_entropy_constrained_test.png'")
else:
    mass = 10  # Solar masses
    distance = 100  # Arbitrary units
    information_density = 0.05  # QIR correction term
    print(f"Entropy-Constrained Effect: {entropy_constrained_scaling(mass, distance, information_density)}")
