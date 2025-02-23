import numpy as np
import matplotlib.pyplot as plt

# Constants
WIDTH, HEIGHT = 400, 400  # Grid resolution
CORNER_A = -15  # Lower-left corner
CORNER_B = -25  # Lower-right corner
SIDE = 41  # Side length of the square grid
NUM_COLORS = 4  # Number of distinct colors


def compute_wallpaper(corner_a, corner_b, side, width, height, num_colors):
    """
    Generate a wallpaper pattern based on squared sums with multiple colors.
    """

    # Set a seed for reproducibility (optional)
    # np.random.seed(0)

    colors = np.random.randint(0, 256, (num_colors, 3), dtype=np.uint8)# Randomly generate distinct RGB colors

    # Create coordinate grids using broadcasting (no need for meshgrid)
    x = corner_a + np.linspace(0, side, width)[:, None] # Column vector (width, 1)
    y = corner_b + np.linspace(0, side, height)[None, :] # Row vector (1, height)
    z = x**2 + y**2 # Compute squared sum pattern
    color_indices = (z % num_colors).astype(np.uint8) # Assign colors cyclically using modulo
    return colors[color_indices]


def plot_wallpaper(image, corner_a, side, corner_b):
    """Plot the generated wallpaper pattern."""
    plt.figure(figsize=(8, 8))
    plt.imshow(image, extent=[corner_a, corner_a +
               side, corner_b, corner_b + side])
    plt.axis('off')
    plt.show()


def main():
    """Main function to execute the wallpaper generation."""
    image = compute_wallpaper(CORNER_A, CORNER_B, SIDE,
                              WIDTH, HEIGHT, NUM_COLORS)
    plot_wallpaper(image, CORNER_A, SIDE, CORNER_B)


if __name__ == "__main__":
    main()
