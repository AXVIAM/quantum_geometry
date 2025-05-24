import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Define parameters
size = 512  # Image resolution
density_field_1 = np.random.rand(size, size)  # Generate first cosmic web model
density_field_2 = np.random.rand(size, size)  # Generate second cosmic web model

# Define different smoothing scales for comparison
smoothing_scales = [6, 9, 11, 14]

# Define different color maps for visualization
color_maps = ["plasma", "viridis", "magma", "coolwarm"]

# Prepare results file
results_filename = "compare_cosmic_web_results.txt"

with open(results_filename, "w") as file:
    file.write("Quantum Information Gravity - Cosmic Web Comparison Results\n")
    file.write("-----------------------------------------------------------\n")
    file.write("Smoothing Scale (σ) | Max Density Model 1 | Min Density Model 1 | Mean Density Model 1 | Max Density Model 2 | Min Density Model 2 | Mean Density Model 2\n")

    # Generate and save images for each smoothing scale and colormap combination
    for sigma in smoothing_scales:
        smoothed_density_1 = gaussian_filter(density_field_1, sigma=sigma)
        smoothed_density_2 = gaussian_filter(density_field_2, sigma=sigma)

        # Compute statistics
        max_density_1 = np.max(smoothed_density_1)
        min_density_1 = np.min(smoothed_density_1)
        mean_density_1 = np.mean(smoothed_density_1)

        max_density_2 = np.max(smoothed_density_2)
        min_density_2 = np.min(smoothed_density_2)
        mean_density_2 = np.mean(smoothed_density_2)

        # Log results
        file.write(f"{sigma} | {max_density_1:.6f} | {min_density_1:.6f} | {mean_density_1:.6f} | {max_density_2:.6f} | {min_density_2:.6f} | {mean_density_2:.6f}\n")

        for cmap in color_maps:
            plt.figure(figsize=(10, 5))

            # Plot first model
            plt.subplot(1, 2, 1)
            plt.imshow(smoothed_density_1, cmap=cmap, origin="lower")
            plt.colorbar(label="Density Contrast")
            plt.title(f"Cosmic Web Model 1 (σ={sigma}, cmap={cmap})")
            plt.xlabel("X Coordinate")
            plt.ylabel("Y Coordinate")

            # Plot second model
            plt.subplot(1, 2, 2)
            plt.imshow(smoothed_density_2, cmap=cmap, origin="lower")
            plt.colorbar(label="Density Contrast")
            plt.title(f"Cosmic Web Model 2 (σ={sigma}, cmap={cmap})")
            plt.xlabel("X Coordinate")
            plt.ylabel("Y Coordinate")

            # Save the figure
            image_filename = f"compare_cosmic_web_sigma_{sigma}_cmap_{cmap}.png"
            plt.savefig(image_filename, dpi=300)
            plt.close()

print(f"✅ Script updated successfully.\nResults saved in {results_filename}\nGenerated multiple cosmic web comparison images.")
