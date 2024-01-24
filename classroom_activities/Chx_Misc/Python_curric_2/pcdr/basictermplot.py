import numpy as np
from typing import Optional, TextIO
import sys
from typeguard import typechecked
from io import StringIO



def rescale(arry: np.ndarray, lower_limit: int, upper_limit: int):
    """
    Rescale data to given bounds.
    Example 1:
    >>> data = np.array([0, 20, 30])
    >>> rescale(data, 0, 3)
    array([0., 2., 3.])
    >>> rescale(data, 0, 6)
    array([0., 4., 6.])
    >>> rescale(data, -3, 3)
    array([-3.,  1.,  3.])

    Example 2:
    >>> d2 = np.array([-20, 0, 30])
    >>> rescale(d2, -2, 3)
    array([-2.,  0.,  3.])
    >>> rescale(d2, 0, 5)
    array([0., 2., 5.])

    (If this is implemented already in the std library
     or a lightweight dep, feel free to submit a pull
     request to use that instead.)
    """
    _max = np.max(arry)
    _min = np.min(arry)
    scale_factor = (upper_limit - lower_limit) / (_max - _min)
    rescaled = (arry - _min) * scale_factor
    return rescaled + lower_limit



@typechecked    
def plot(xs: np.ndarray, ys: np.ndarray, xoutputsize: Optional[int] = None, youtputsize: int = 8, round_ndigits: int = 2, output_stream: Optional[TextIO] = None) -> None:
    """
    A basic plot function, used primarily for docstring (and doctest) examples.
    
    >>> xs = np.array([0, 10])
    >>> ys = np.array([0, 30])
    >>> plot(xs, ys, 2, 2)
    xmin: 0
    xmax: 10
    ymin: 0
    ymax: 30
    ~█o
    ~o█

    >>> xs = np.array([0, 20, 30])
    >>> ys = np.array([0, 20, 10])
    >>> plot(xs, ys, 4, 3)
    xmin: 0
    xmax: 30
    ymin: 0
    ymax: 20
    ~██o█
    ~███o
    ~o███

    >>> xs = np.array([ 0, 10, 20, 40, 50, 60, 70])
    >>> ys = np.array([20, 30, 20, 20, 10,  0,  0])
    >>> plot(xs, ys, xoutputsize=8, youtputsize=4)
    xmin: 0
    xmax: 70
    ymin: 0
    ymax: 30
    ~█o██████
    ~o█o█o███
    ~█████o██
    ~██████oo

    This won't allow complex data, but one option is to just plot the real part.
    >>> xs = np.array([ 1, 2])
    >>> ys = np.array([ 1 + 2j, 10 + 20j])
    >>> plot(xs, ys)
    Traceback (most recent call last):
      ...
    ValueError: ...
    """
    
    if np.iscomplex(xs).any():
        raise ValueError("Complex values are not allowed")
    if np.iscomplex(ys).any():
        raise ValueError("Complex values are not allowed")
    
    if xoutputsize == None:
        xoutputsize = len(xs)
        
    assert isinstance(xoutputsize, int)

    drawing = np.zeros((youtputsize, xoutputsize))

    scaledx = np.uint16(rescale(xs, 0, xoutputsize - 1))
    scaledy = np.uint16(rescale(ys, 0, youtputsize - 1))
    # scaledx = np.uint16(xs * scale_factor_x)
    # scale_factor_y = (youtputsize - 1) / maxy
    # scaledy = np.uint16(ys * scale_factor_y)
    assert isinstance(scaledx, np.ndarray)
    assert isinstance(scaledy, np.ndarray)
    assert (0 <= scaledx).all()
    assert (scaledx < xoutputsize).all()
    assert (0 <= scaledy).all()
    assert (scaledy < youtputsize).all()
    
    invertedy = youtputsize - scaledy - 1
    assert (0 <= invertedy).all()
    assert (invertedy < youtputsize).all()
    
    drawing[invertedy, scaledx] = 1

    @typechecked
    def printstream(x: str = "", end: str = "\n"):
        if output_stream == None:
            print(x, end=end)
        else:
            print(x, end=end, file=output_stream)

    printstream(f"xmin: {round(np.min(xs), round_ndigits)}")
    printstream(f"xmax: {round(np.max(xs), round_ndigits)}")
    printstream(f"ymin: {round(np.min(ys), round_ndigits)}")
    printstream(f"ymax: {round(np.max(ys), round_ndigits)}")
    for row in drawing:
        printstream("~", end="")
        for item in row:
            c = "o" if item == 1 else "█"
            printstream(c, end="")
        printstream()
