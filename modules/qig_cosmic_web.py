import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Define parameters
size = 512  # Image resolution
density_field = np.random.rand(size, size)  # Generate a random density field

# Define different smoothing scales
smoothing_scales = [5, 8, 10, 12]

# Define different color maps for visualization
color_maps = ["plasma", "viridis", "magma", "coolwarm"]

# Prepare results file
results_filename = "qig_cosmic_web_results.txt"

with open(results_filename, "w") as file:
    file.write("Quantum Information Gravity - Cosmic Web Structure Results\n")
    file.write("-----------------------------------------------------------\n")
    file.write("Smoothing Scale (σ) | Max Density | Min Density | Mean Density\n")

    # Generate and save images for each smoothing scale and colormap combination
    for sigma in smoothing_scales:
        smoothed_density = gaussian_filter(density_field, sigma=sigma)

        # Compute statistics
        max_density = np.max(smoothed_density)
        min_density = np.min(smoothed_density)
        mean_density = np.mean(smoothed_density)

        # Log results
        file.write(f"{sigma} | {max_density:.6f} | {min_density:.6f} | {mean_density:.6f}\n")

        for cmap in color_maps:
            plt.figure(figsize=(8, 8))
            plt.imshow(smoothed_density, cmap=cmap, origin="lower")
            plt.colorbar(label="Density Contrast")
            plt.title(f"Cosmic Web Structure (σ={sigma}, cmap={cmap})")
            plt.xlabel("X Coordinate")
            plt.ylabel("Y Coordinate")

            # Save the figure
            image_filename = f"qig_cosmic_web_sigma_{sigma}_cmap_{cmap}.png"
            plt.savefig(image_filename, dpi=300)
            plt.close()

print(f"✅ Script updated successfully.\nResults saved in {results_filename}\nGenerated multiple image outputs.")
