Clipping happens when the signal is larger than the ADC is able to measure. Example:

```python3
import pyqtgraph as pg
import numpy as np
from pcdr.unstable import make_wave

def clip_to_1(dat: np.ndarray) -> np.ndarray:
    cop = dat.copy()
    cop[cop>1] = 1
    cop[cop<-1] = -1
    return cop

samp_rate = 100
seconds = 2
wave = make_wave("real", samp_rate, freq=3, seconds=seconds)
x = wave.x
y_rescaled = 1.2 * wave.y
y_clipped = clip_to_1(y_rescaled)
## TODO: make these on the same plot with two colors
pg.plot(x, y_rescaled)
pg.plot(x, y_clipped)



```
