import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt
from dataclasses import dataclass

from demo import utils
from demo import constants


@dataclass
class JSONExample:
    """
    Dataclass for each JSON example
    """
    path: str

    def __post_init__(self):
        # Load the training and testing data from the JSON file
        json_data = utils.load_json(self.path)
        self.train = json_data["train"]
        self.test = json_data["test"][0]

    def plot_demonstrations(self, fig_w: int = constants.PLOT_W, fig_h: int = constants.PLOT_H, **kwargs) -> plt.Figure:
        """
        Plots the training demonstration examples
        """
        ncols = 2
        nrows = len(self.train)
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * fig_w, nrows * fig_h))
        fig.suptitle("Example Demonstrations")
        axes = axes.flatten()
        for i, example_dict in enumerate(self.train):
            input_ax, output_ax = axes[2 * i:2 * (i + 1)]
            if i == 0:
                input_ax.set_title("Input Grid")
                output_ax.set_title("Output Grid")
            utils.plot_example(input_ax, example_dict["input"], **kwargs)
            utils.plot_example(output_ax, example_dict["output"], **kwargs)
        return fig


@dataclass
class AnswerGrid:
    """
    Dataclass to handle the answering grid
    """
    data: np.ndarray
    vmax: int = constants.VMAX

    @staticmethod
    def resize(array: np.ndarray, shape: Tuple[int, int]) -> np.ndarray:
        """
        Resizes the current data array to given shape by preserving previous data
        """
        new_width, new_height = shape
        old_width, old_height = array.shape
        min_w = min(old_width, new_width)
        min_h = min(old_height, new_height)
        new_data = np.zeros((new_height, new_width), dtype="uint8")
        new_data[:min_h, :min_w] = array[:min_h, :min_w]
        return new_data

    @property
    def shape(self) -> Tuple[int, int]:
        return self.data.shape

    @shape.setter
    def shape(self, value: Tuple[int, int]):
        assert len(value) == 2, f"Shape should be a tuple of (width, height). Instead received {value}!"
        self.data = self.resize(self.data, value)

    def is_valid_pos(self, x: int, y: int) -> bool:
        """
        Check that given xy coordinates lies on the current array
        """
        height, width = self.data.shape
        return (0 <= x < width) and (0 <= y < height)

    def increase(self, x: int, y: int):
        """
        Increase the pixel value at given coordinate by 1
        """
        if self.is_valid_pos(x, y):
            self.data[y, x] = (self.data[y, x] + 1) % self.vmax

    def decrease(self, x: int, y: int):
        """
        Decrease the pixel value at given coordinate by 1
        """
        if self.is_valid_pos(x, y):
            self.data[y, x] = (self.data[y, x] - 1) % self.vmax

    def check(self, output_array: np.ndarray) -> bool:
        """
        Check if given output array matches the answer array
        """
        return np.array_equal(self.data, output_array)
