from matplotlib import colors


PLOT_W = PLOT_H = 4                             # Plot dimensions
MIN_NUM_GRID, MAX_NUM_GRID = 1, 30              # Min-Max grid size
# Grid colors for values in the range 0-9
COLORS = ["black", "lightblue", "red", "green", "yellow", "grey", "pink", "orange", "teal", "brown"]
NUM_COLORS = len(COLORS)
BOUNDS = list(range(NUM_COLORS))                # Bound for the color map
VMAX = NUM_COLORS - 1                           # Maximum pixel value
COLOR_KWARGS = {
    "cmap": colors.ListedColormap(COLORS),
    "norm": colors.BoundaryNorm(BOUNDS, NUM_COLORS),
}
