# Wallpaper Pattern Generator, ***Wallpaper for the Mind***

![Circle](circle_1.png)

## Historical Context

This Python script generates visually stunning wallpaper patterns based on a mathematical algorithm developed by John E. Connett. The algorithm was introduced in A.K. Dewdney's "Computer Recreations" column in *Scientific American* (September 1986), where he coined the name **Circle²** for this method. It explores the mathematical properties of grid-based coordinate systems and the equation:

$$
\large
z = x² + y²
\large
$$

The **Circle² algorithm** visualizes the distribution of squared sums `z = x² + y²` for a structured grid of coordinates `(x, y)`. By assigning colors based on the properties of `z`, the algorithm creates concentric circular patterns.

### How It Works

This algorithm computes a grid-based wallpaper pattern by evaluating the function:

$$
z = x² + y²
$$

for each grid point `(x, y)`, where `x` and `y` are derived from a scaled coordinate system.  
The integer part of `z` (or its modulo operation) is used to assign colors cyclically from a predefined palette.

#### **Approach**

1. **Grid Construction**:
   - The grid spans a defined rectangular area, with `x` and `y` values computed based on a scaling factor.
   - In the **historical loop-based version**, this is done iteratively for each pixel.
   - In the **optimized NumPy version**, this is achieved efficiently using **vectorized operations**.

2. **Squared Sum Computation**:
   - Each coordinate pair is mapped to `z = x² + y²`, where `x` and `y` are **not necessarily integers** but follow a structured grid pattern.

3. **Color Assignment**:
   - The integer part of `z` or its modulo operation `z modulo NUM_COLORS` cycles through a fixed color palette.
   - The **historical version** explicitly converts `z` to an integer before applying modulo, while the **optimized version** lets **NumPy handle it** directly.

### Customization

Adjust the following parameters to create unique designs:

- **WIDTH, HEIGHT**: Resolution of the image.
- **CORNER_A, CORNER_B**: Lower-left corner of the grid.
- **SIDE**: Side length of the grid.
- **NUM_COLORS**: Number of colors in the palette.
