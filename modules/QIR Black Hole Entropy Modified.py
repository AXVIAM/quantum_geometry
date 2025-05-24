import numpy as np
import matplotlib.pyplot as plt

# Universal counterweight value
C = 0.90  # Adjusts all QIR predictions by a fixed percentage

# QIR Black Hole Entropy Model with Universal Counterweight
def black_hole_entropy_correction(mass, qir_correction):
    return (mass ** 2) * (1 + qir_correction) * C  # Apply universal correction

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Black hole entropy data from LIGO or EHT
    observed_masses = np.array([10, 12, 15])  # Replace with actual dataset values
    observed_qir_correction = np.array([0.01, 0.02, 0.03])  # Replace with actual dataset values
    observed_entropies = np.array([100.5, 144.0, 225.5])  # Replace with real entropy values
    
    predicted_entropies = [black_hole_entropy_correction(m, c) for m, c in zip(observed_masses, observed_qir_correction)]
    
    # Save results to TXT file
    with open("output_entropy_comparison_modified.txt", "w") as file:
        file.write("Observed Data vs. QIR Predictions (With Universal Counterweight)\n")
        file.write("Mass (Solar Masses) | QIR Correction | Observed Entropy | QIR-Predicted Entropy (Corrected)\n")
        for m, qc, oe, pe in zip(observed_masses, observed_qir_correction, observed_entropies, predicted_entropies):
            file.write(f"{m:.2f} | {qc:.4f} | {oe:.4f} | {pe:.4f}\n")

    # Plot real vs. simulated data
    plt.scatter(observed_masses, observed_entropies, color='red', label="Observed Black Hole Entropy")
    plt.scatter(observed_masses, predicted_entropies, color='blue', label="QIR-Predicted Entropy (Corrected)")
    plt.xlabel("Mass (Solar Masses)")
    plt.ylabel("Black Hole Entropy")
    plt.title("QIR Black Hole Entropy vs. Observed Data (With Correction)")
    plt.legend()
    plt.savefig("output_entropy_comparison_modified.png")

    print("Results saved as 'output_entropy_comparison_modified.txt' and 'output_entropy_comparison_modified.png'")
else:
    mass = 10  # Solar masses
    qir_correction = 0.02  # QIR entropy correction term
    print(f"Black hole entropy correction: {black_hole_entropy_correction(mass, qir_correction)}")
