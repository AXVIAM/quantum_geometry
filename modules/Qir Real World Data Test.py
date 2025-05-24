import numpy as np
import matplotlib.pyplot as plt

# QIR Scaling Model for Testing Against Real-World Data
C = np.pi  # Pi remains fundamental as a geometric constraint

def real_world_qir_scaling(mass, distance, information_density):
    # Apply the validated scaling function for real-world testing
    scale_factor = C * (mass ** 1.792) * (distance ** 0.421) * (information_density ** -0.512)
    # Apply entropy-based self-regulation
    return scale_factor / (1 + np.log(1 + (mass * distance * information_density)))

# Load real-world dataset (example format, replace with actual dataset path)
real_world_data = np.loadtxt("real_world_data.txt", delimiter=",", skiprows=1)  # Assumes CSV format: mass, distance, information_density, observed_value

# Extract data columns
masses = real_world_data[:, 0]
distances = real_world_data[:, 1]
information_densities = real_world_data[:, 2]
observed_values = real_world_data[:, 3]

# Compute QIR predictions
qir_predictions = [real_world_qir_scaling(m, d, I) for m, d, I in zip(masses, distances, information_densities)]

# Save results to TXT file
with open("output_real_world_qir_test.txt", "w") as file:
    file.write("Real-World Data vs. QIR Predictions\n")
    file.write("Mass (Solar Masses) | Distance (Units) | Information Density | Observed Value | QIR-Predicted Value\n")
    for m, d, I, ov, pv in zip(masses, distances, information_densities, observed_values, qir_predictions):
        file.write(f"{m:.2f} | {d:.2f} | {I:.4f} | {ov:.4f} | {pv:.4f}\n")

# Plot real-world observed data vs. QIR predictions
plt.scatter(distances, observed_values, color='red', label="Observed Data")
plt.scatter(distances, qir_predictions, color='blue', label="QIR-Predicted Values")
plt.xlabel("Distance")
plt.ylabel("Effect Magnitude")
plt.title("QIR Predictions vs. Real-World Data")
plt.legend()
plt.savefig("output_real_world_qir_test.png")

print("Results saved as 'output_real_world_qir_test.txt' and 'output_real_world_qir_test.png'")
