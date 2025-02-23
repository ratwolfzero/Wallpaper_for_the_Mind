import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
WIDTH, HEIGHT = 400, 400  # Grid resolution
CORNER_A = -15  # Lower-left corner
CORNER_B = -25  # Lower-right corner
SIDE = 41  # Side length of the square grid
NUM_COLORS = 4  # Number of distinct colors

# Set the seed for random module (optional)
# random.seed(0)


def compute_wallpaper(corner_a, corner_b, side, width, height, num_colors):
    """Compute a pattern based on squared sums with multiple colors."""
    image = np.zeros((height, width, 3), dtype=np.uint8)  # RGB Image
    colors = []

    for _ in range(num_colors):
        colors.append([random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255)])

    for i in range(height):
        for j in range(width):
            x = corner_a + (side * i / width)
            y = corner_b + (side * j / height)
            z = x**2 + y**2
            c = int(z)

            color_index = c % num_colors  # Use modulo to cycle through colors
            image[i, j] = colors[color_index]

    return image


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
