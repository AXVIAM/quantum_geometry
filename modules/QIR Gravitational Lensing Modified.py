import numpy as np
import matplotlib.pyplot as plt

# Universal counterweight value
C = 0.90  # Adjusts all QIR predictions by a fixed percentage

# QIR Lensing Model with Universal Counterweight
def lensing_effect(mass, distance, alpha):
    return ( (4 * mass / distance) + alpha ) * C  # Apply universal correction

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Sloan Digital Sky Survey lensing values
    observed_masses = np.array([1.2, 1.5, 1.8])  # Replace with actual dataset values
    observed_distances = np.array([110, 95, 130])  # Replace with actual dataset values
    observed_lensing = np.array([0.08, 0.1, 0.12])  # Replace with real lensing values
    
    predicted_lensing = [lensing_effect(m, d, 0.05) for m, d in zip(observed_masses, observed_distances)]
    
    # Save results to TXT file
    with open("output_lensing_comparison_modified.txt", "w") as file:
        file.write("Observed Data vs. QIR Predictions (With Universal Counterweight)\n")
        file.write("Mass (Solar Masses) | Distance (Units) | Observed Lensing | QIR-Predicted Lensing (Corrected)\n")
        for m, d, ol, pl in zip(observed_masses, observed_distances, observed_lensing, predicted_lensing):
            file.write(f"{m:.2f} | {d:.2f} | {ol:.4f} | {pl:.4f}\n")

    # Plot real vs. simulated data
    plt.scatter(observed_distances, observed_lensing, color='red', label="Observed Lensing")
    plt.scatter(observed_distances, predicted_lensing, color='blue', label="QIR-Predicted Lensing (Corrected)")
    plt.xlabel("Distance")
    plt.ylabel("Lensing Effect")
    plt.title("QIR Gravitational Lensing vs. Observed Data (With Correction)")
    plt.legend()
    plt.savefig("output_lensing_comparison_modified.png")

    print("Results saved as 'output_lensing_comparison_modified.txt' and 'output_lensing_comparison_modified.png'")
else:
    mass = 1.0  # Solar masses
    distance = 100  # Arbitrary units
    alpha = 0.05  # QIR correction term
    print(f"Lensing effect: {lensing_effect(mass, distance, alpha)}")
