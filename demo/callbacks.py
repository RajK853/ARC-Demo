import numpy as np
from typing import Dict
from matplotlib.pyplot import Axes
from ipywidgets import IntSlider, Button
from matplotlib.backend_bases import MouseEvent

from demo.utils import plot_example
from demo.dataclasses import JSONExample, AnswerGrid


def onclick(ax: Axes, ans_grid: AnswerGrid, width: IntSlider, height: IntSlider, color_kwargs: Dict, event: MouseEvent):
    """
    Callback function to handle mouse event on the image
    """
    # Round over (floor) the xy-coordinates
    x = int(np.floor(event.xdata))
    y = int(np.floor(event.ydata))
    if event.button == 1:               # Left click
        ans_grid.decrease(x, y)
    elif event.button == 2:             # Wheel click
        ans_grid.shape = (width.value, height.value)
    elif event.button == 3:             # Right click
        ans_grid.increase(x, y)
    plot_example(ax, ans_grid.data, hide_ticks=False, **color_kwargs)


def check_answer(example: JSONExample, ans_grid: AnswerGrid, event: Button):
    """
    Callback for check answer button
    """
    if ans_grid.check(example.test["output"]):
        event.style.button_color = 'lightgreen'
    else:
        event.style.button_color = 'red'
