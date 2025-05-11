# Wallpaper Pattern Generator – ***Wallpaper for the Mind***

![Circle](circle_1.png)

## Historical Context

This Python script generates visually striking patterns based on the algorithm known as Circle². The underlying mathematical idea was developed by John E. Connett, a biostatistician at the University of Minnesota. The method was later popularized and named "Circle²" by A.K. Dewdney in his Computer Recreations column in Scientific American (September 1986). The method explores the mathematical beauty of the equation:

$$
\large z = x^2 + y^2
$$

By applying this formula across a grid of coordinates and assigning colors based on the result, it produces hypnotic, circular wallpaper designs.

## Algorithm Overview

At the heart of the pattern is the squared sum of coordinates:

$$
z = x^2 + y^2
$$

Each point `(x, y)` on a grid is evaluated using this equation. The value of `z` is then either directly converted to an integer or used with a modulo operation to index into a color palette, creating cyclical, ring-like patterns.

* **Grid Construction**: A rectangular grid is defined using customizable corner and size parameters. In the optimized version, this grid is built using NumPy for speed and efficiency.

* **Computation & Coloring**:

  * `z` is computed at each grid point.
  * Colors are assigned by taking `int(z) % NUM_COLORS`, cycling through a fixed palette.
  * The classic version used loops; the current version uses vectorized operations for faster rendering.

## Customization

You can tweak these parameters to generate unique visual styles:

* **WIDTH, HEIGHT**: Image resolution.
* **CORNER\_A, CORNER\_B**: Coordinates of the lower-left corner of the grid.
* **SIDE**: Length of the square grid area.
* **NUM\_COLORS**: Number of distinct colors in the palette.


