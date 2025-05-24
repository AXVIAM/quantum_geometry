import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Generate a simulated cosmic web density field
np.random.seed(42)
size = 512  # Image resolution
density_field = np.random.rand(size, size)

# Define different smoothing scales
smoothing_scales = [5, 8, 10, 12]

# Define different color maps for comparison
color_maps = ["plasma", "viridis", "magma", "coolwarm"]

# Generate images for each smoothing scale and colormap combination
for sigma in smoothing_scales:
    smoothed_density = gaussian_filter(density_field, sigma=sigma)

    for cmap in color_maps:
        plt.figure(figsize=(8, 8))
        plt.imshow(smoothed_density, cmap=cmap, origin="lower")
        plt.colorbar(label="Density Contrast")
        plt.title(f"Cosmic Web (σ={sigma}, cmap={cmap})")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")

        # Save the figure
        filename = f"Cosmic_Web_sigma_{sigma}_cmap_{cmap}.png"
        plt.savefig(filename, dpi=300)
        plt.close()

        print(f"Saved: {filename}")

print("All images have been generated and saved.")