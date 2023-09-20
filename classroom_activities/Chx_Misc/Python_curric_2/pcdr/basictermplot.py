import numpy as np

    
def plot(xs: np.ndarray, ys: np.ndarray, xoutputsize: int = 30, youtputsize: int = 8) -> None:
    """
    A basic plot function, used primarily for docstring (and doctest) examples.

    xmin and ymin are always zero.
    
    >>> xs = np.array([0, 10])
    >>> ys = np.array([0, 10])
    >>> plot(xs, ys, 2, 2)
     o
    o 

    >>> xs = np.array([0, 20, 30])
    >>> ys = np.array([0, 20, 10])
    >>> plot(xs, ys, 4, 3)
      o 
       o
    o   

    >>> xs = np.array([ 0, 10, 20, 40, 50, 60, 70])
    >>> ys = np.array([20, 30, 20, 20, 10,  0,  0])
    >>> plot(xs, ys, xoutputsize=8, youtputsize=4)
     o      
    o o o   
         o  
          oo
    
    >>> xs = np.linspace()
    """
    drawing = np.zeros((youtputsize, xoutputsize))

    scale_factor_x = (xoutputsize - 1) / max(xs)
    scale_factor_y = (youtputsize - 1) / max(ys)
    scaledx = np.uint16(xs * scale_factor_x)
    scaledy = np.uint16(ys * scale_factor_y)
    invertedy = youtputsize - scaledy - 1
    drawing[invertedy, scaledx] = 1
    for row in drawing:
        for item in row:
            c = "o" if item == 1 else " "
            print(c, end="")
        print()




