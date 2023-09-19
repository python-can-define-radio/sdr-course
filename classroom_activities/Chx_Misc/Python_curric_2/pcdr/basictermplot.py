import numpy as np


    
def plot(xs: np.ndarray, ys: np.ndarray, xoutputsize: int = 30, youtputsize: int = 8) -> None:
    """
    A basic plot function, used primarily for docstring (and doctest) examples.

    xmin and ymin are always zero.

    >>> xs = np.array([20, 30, 40, 50, 60])
    >>> ys = np.array([10, 20, 10,  0,  0])
    >>> plot(xs, ys, xoutputsize=7, youtputsize=3)
       o
      o o
         oo
    """
    drawing = np.zeros((youtputsize, xoutputsize))

    scaledx = np.uint16(xs * xoutputsize / max(xs))
    scaledy = np.uint16(ys * youtputsize / max(ys))
    drawing[scaledx, scaledy] = 1
    print(drawing)
