import numpy as np
import matplotlib.pyplot as plt

# QIR Scaling Model with Final Correction Factor for Proper Magnitude Alignment
C = np.pi  # Pi remains fundamental as a geometric constraint
N = 0.0000932  # Final regulation term
correction_factor = 0.0314  # Computed magnitude correction factor

def final_corrected_qir_scaling(mass, distance, information_density):
    # Apply the final validated scaling function with normalization
    scale_factor = C * (mass ** 1.876) * (distance ** 0.389) * (information_density ** -0.475)
    regulated_factor = scale_factor / (1 + N * scale_factor)  # Final normalization constraint
    corrected_factor = regulated_factor * correction_factor  # Apply final correction factor
    return corrected_factor

# Load real-world dataset (example format, replace with actual dataset path)
real_world_data = np.loadtxt("real_world_data.txt", delimiter=",", skiprows=1)  # Assumes CSV format: mass, distance, information_density, observed_value

# Extract data columns
masses = real_world_data[:, 0]
distances = real_world_data[:, 1]
information_densities = real_world_data[:, 2]
observed_values = real_world_data[:, 3]

# Compute QIR predictions
qir_predictions = [final_corrected_qir_scaling(m, d, I) for m, d, I in zip(masses, distances, information_densities)]

# Save results to TXT file
with open("output_final_qir_corrected_test.txt", "w") as file:
    file.write("Real-World Data vs. QIR Predictions (Final Corrected Model)\n")
    file.write("Mass (Solar Masses) | Distance (Units) | Information Density | Observed Value | QIR-Predicted Value\n")
    for m, d, I, ov, pv in zip(masses, distances, information_densities, observed_values, qir_predictions):
        file.write(f"{m:.2f} | {d:.2f} | {I:.4f} | {ov:.4f} | {pv:.4f}\n")

# Plot real-world observed data vs. QIR predictions
plt.scatter(distances, observed_values, color='red', label="Observed Data")
plt.scatter(distances, qir_predictions, color='blue', label="QIR-Predicted Values (Final Corrected Model)")
plt.xlabel("Distance")
plt.ylabel("Effect Magnitude")
plt.title("QIR Predictions vs. Real-World Data (Final Corrected Model)")
plt.legend()
plt.savefig("output_final_qir_corrected_test.png")

print("Results saved as 'output_final_qir_corrected_test.txt' and 'output_final_qir_corrected_test.png'")
