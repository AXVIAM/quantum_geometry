import numpy as np
import scipy.optimize as opt

# Observed vs QIR-predicted values from our tests
observed_values = {
    "lensing": np.array([0.0800, 0.1000, 0.1200]),  # Observed lensing effects
    "entropy": np.array([100.50, 144.00, 225.50]),  # Observed black hole entropy
    "uncertainty": np.array([5.0000, 3.0000, 2.5000])  # Observed quantum uncertainty
}

qir_predicted_values = {
    "lensing": np.array([0.0936, 0.1132, 0.1054]),  # QIR-predicted lensing effects
    "entropy": np.array([101.00, 146.88, 231.75]),  # QIR-predicted black hole entropy
    "uncertainty": np.array([5.0000, 3.0000, 1.6667])  # QIR-predicted quantum uncertainty
}

# Corresponding mass, distance, and information density values
masses = np.array([1.2, 1.5, 1.8])  # Mass in solar masses for lensing and entropy
distances = np.array([110, 95, 130])  # Distances for lensing
information_density = np.array([0.04, 0.05, 0.06])  # Information density values for uncertainty

# Define the balancing equation model

def balancing_equation(params, m, d, I, qir_predictions):
    C, a, b, c = params  # Parameters to optimize
    return C * (m ** a) * (d ** b) * (I ** c) - qir_predictions

# Initial guesses for C, a, b, c
initial_guess = [1.0, 0.5, -0.5, 0.5]

# Flatten observed and predicted values for curve fitting
observed_data = np.concatenate((observed_values["lensing"], observed_values["entropy"], observed_values["uncertainty"]))
predicted_data = np.concatenate((qir_predicted_values["lensing"], qir_predicted_values["entropy"], qir_predicted_values["uncertainty"]))
m_all = np.concatenate((masses, masses, masses))
d_all = np.concatenate((distances, distances, distances))
I_all = np.concatenate((information_density, information_density, information_density))

# Perform least squares optimization to fit C, a, b, c
optimal_params = opt.least_squares(balancing_equation, initial_guess, args=(m_all, d_all, I_all, predicted_data)).x
C_opt, a_opt, b_opt, c_opt = optimal_params

# Display results
print(f"Optimal C: {C_opt}")
print(f"Optimal a: {a_opt}")
print(f"Optimal b: {b_opt}")
print(f"Optimal c: {c_opt}")

# Save results to a text file
with open("output_balancing_equation_fit.txt", "w") as file:
    file.write(f"Optimal C: {C_opt}\n")
    file.write(f"Optimal a: {a_opt}\n")
    file.write(f"Optimal b: {b_opt}\n")
    file.write(f"Optimal c: {c_opt}\n")

print("Results saved to output_balancing_equation_fit.txt")
