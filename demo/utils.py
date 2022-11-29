import json
from typing import Dict

import numpy as np
from matplotlib.pyplot import Axes


def load_json(path: str) -> Dict:
    """
    Load JSON file
    """
    with open(path, "r") as fp:
        return json.load(fp)


def plot_example(ax: Axes, grid_values: np.ndarray, hide_ticks: bool = True, **kwargs) -> Axes:
    """
    Plot the grid values on the given axes
    """
    nrows, ncols = np.shape(grid_values)
    ax.imshow(grid_values, origin="lower", extent=[0, ncols, 0, nrows], **kwargs)
    ax.set_xticks(range(ncols))
    ax.set_yticks(range(nrows))
    if hide_ticks:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    ax.grid(True, color="grey", alpha=1.0)
    return ax
