import numpy as np
import matplotlib.pyplot as plt

# QIR Scaling Model Using Fractal-Based Recursive Scaling
C = np.pi  # Pi as a fundamental scaling constant

# Define the fractal-based scaling function
def fractal_scaling(mass, distance, information_density, iterations=5):
    result = mass * distance / (1 + information_density)  # Initial scaling function
    for _ in range(iterations):
        result = C * np.log(1 + result)  # Recursive fractal-like transformation
    return result

# Allow user input of real-world data
use_real_data = input("Use real-world data? (yes/no): ").strip().lower() == "yes"

if use_real_data:
    # Example: Black hole entropy, lensing, and quantum uncertainty data
    observed_masses = np.array([10, 12, 15])  # Replace with actual dataset values
    observed_distances = np.array([110, 95, 130])  # Replace with actual dataset values
    observed_information_density = np.array([0.04, 0.05, 0.06])  # Replace with actual dataset values
    observed_values = np.array([100.5, 144.0, 225.5])  # Replace with real observed values
    
    predicted_values = [fractal_scaling(m, d, I) for m, d, I in zip(observed_masses, observed_distances, observed_information_density)]
    
    # Save results to TXT file
    with open("output_fractal_scaling_test.txt", "w") as file:
        file.write("Observed Data vs. QIR Predictions (With Fractal Scaling)\n")
        file.write("Mass (Solar Masses) | Distance (Units) | Information Density | Observed Value | QIR-Predicted Value (Corrected)\n")
        for m, d, I, ov, pv in zip(observed_masses, observed_distances, observed_information_density, observed_values, predicted_values):
            file.write(f"{m:.2f} | {d:.2f} | {I:.4f} | {ov:.4f} | {pv:.4f}\n")

    # Plot real vs. simulated data
    plt.scatter(observed_distances, observed_values, color='red', label="Observed Data")
    plt.scatter(observed_distances, predicted_values, color='blue', label="QIR-Predicted Values (Fractal Scaling)")
    plt.xlabel("Distance")
    plt.ylabel("Effect Magnitude")
    plt.title("QIR Predictions vs. Observed Data (Fractal Scaling Model)")
    plt.legend()
    plt.savefig("output_fractal_scaling_test.png")

    print("Results saved as 'output_fractal_scaling_test.txt' and 'output_fractal_scaling_test.png'")
else:
    mass = 10  # Solar masses
    distance = 100  # Arbitrary units
    information_density = 0.05  # QIR correction term
    print(f"Fractal Scaling Effect: {fractal_scaling(mass, distance, information_density)}")
