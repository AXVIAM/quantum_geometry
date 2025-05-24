import numpy as np
import matplotlib.pyplot as plt

# QIR Quantum Uncertainty Model
def quantum_uncertainty(position_uncertainty, information_density):
    return (1 / information_density) * position_uncertainty  # Placeholder equation

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Quantum fluctuation data from LHC or NIST
    observed_uncertainties = np.array([0.2, 0.15, 0.1])  # Replace with actual dataset values
    observed_information_density = np.array([0.04, 0.05, 0.06])  # Replace with actual dataset values
    observed_results = np.array([5.0, 3.0, 2.5])  # Replace with real uncertainty values
    
    predicted_results = [quantum_uncertainty(u, d) for u, d in zip(observed_uncertainties, observed_information_density)]
    
    # Save results to TXT file
    with open("output_uncertainty_comparison.txt", "w") as file:
        file.write("Observed Data vs. QIR Predictions\n")
        file.write("Position Uncertainty | Information Density | Observed Uncertainty | QIR-Predicted Uncertainty\n")
        for ou, od, orr, pr in zip(observed_uncertainties, observed_information_density, observed_results, predicted_results):
            file.write(f"{ou:.2f} | {od:.2f} | {orr:.4f} | {pr:.4f}\n")

    # Plot real vs. simulated data
    plt.scatter(observed_information_density, observed_results, color='red', label="Observed Quantum Uncertainty")
    plt.scatter(observed_information_density, predicted_results, color='blue', label="QIR-Predicted Uncertainty")
    plt.xlabel("Information Density")
    plt.ylabel("Quantum Uncertainty Effect")
    plt.title("QIR Quantum Uncertainty vs. Observed Data")
    plt.legend()
    plt.savefig("output_uncertainty_comparison.png")

    print("Results saved as 'output_uncertainty_comparison.txt' and 'output_uncertainty_comparison.png'")
else:
    position_uncertainty = 1.0  # Arbitrary units
    information_density = 0.05  # QIR correction term
    print(f"Quantum uncertainty effect: {quantum_uncertainty(position_uncertainty, information_density)}")
