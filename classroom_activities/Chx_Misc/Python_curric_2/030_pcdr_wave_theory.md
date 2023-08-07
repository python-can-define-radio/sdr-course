## Wave theory

We've sent some OOK-modulated data. Now, let's graph that data and explore it.

We'll start by simply graphing a wave.

```python3
## 1
## Try this.
import matplotlib.pyplot as plt
from pcdr.wavegen import createTimestamps, makeRealWave

timestamps = createTimestamps(seconds=1.0, num_samples=60)
wave = makeRealWave(timestamps, freq=3)
plt.plot(timestamps, wave, "*", markersize=10)
plt.show()


## 2
## Ask the user for
## - The frequency of the wave to plot
## - The number of samples
## - The amount of time (that is, the number of seconds)
## - (Optional) the markersize
## - (Optional) the marker (currently "*". Valid choices are listed in the matplotlib docs. You can also experiment.)


## 3
## Plot a wave that completes two cycles in 1 second.


## 4
## Plot a wave that completes a cycle in two seconds.
```

Now that we've plotted a wave, let's look back at our `ook_modulate` function.

```python3
## 5
## Try this.
import matplotlib.pyplot as plt
from pcdr.modulators import ook_modulate

modded = ook_modulate(data=[1, 0, 1, 0], bit_length=4)
plt.plot(modded, "*-", markersize=20)
plt.show()


## 6
## Copy and modify the above example so that each bit is 10 samples long.
```

You may be surprised that the `ook_modulate` function doesn't produce a wave. Why were we able to send this data to the Hack RF when it doesn't seem to have a carrier wave? You may remember that when working with the Hack RF, we specify a center frequency (or "Ch0 Frequency"). For any data that you ask it to send, the Hack RF first shifts the data to the specified center frequency. This is known as **upconversion**.

There are cases in which we would like to impose the data on a carrier wave before the Hack RF shifts it. Let's try it:

```python3
## 7
## Try this.
import matplotlib.pyplot as plt
from pcdr.wavegen import createTimestamps, makeRealWave
from pcdr.modulators import ook_modulate

timestamps = createTimestamps(seconds=1.0, num_samples=60)
wave = makeRealWave(timestamps, freq=4)
modded = ook_modulate(data=[1, 0, 1, 0], bit_length=15)
fully_modded = modded * wave
plt.plot(timestamps, fully_modded, "*-", markersize=20)
plt.show()


## 8
## Unfinished exercise
import matplotlib.pyplot as plt
from pcdr.wavegen import createTimestamps, makeRealWave, makeComplexWave
from pcdr.modulators import ook_modulate
from pcdr.gnuradio_sender import gnuradio_send



timestamps = createTimestamps(seconds=1.0, num_samples=int(2e6))
wave = makeComplexWave(timestamps, freq=4)
modded = ook_modulate(data=[1, 0, 1, 0], bit_length=int(500e3))
fully_modded = modded * wave
gnuradio_send(fully_modded, center_freq=100e6, samp_rate=2e6)

## Actual transmission frequency: 100,000,004 Hz = 100.0000004 MHz
plt.plot(timestamps, fully_modded, "*-", markersize=20)
plt.show()
```



```python3
timestamps, y_vals = parse_csv(filename_csv, samp_rate)
plt.plot(timestamps, y_vals, "*", markersize=10)
plt.show()
```


```python3
import numpy as np
import matplotlib.pyplot as plt

import pcdr.wavegen as wavegen

## 1
# pcdr.wave_gen_prompts()
```

```python3
# pcdr.plot_from_csv("generated_data.csv", 100)


## 2
wavegen.wave_gen(100, 3, 2, "r", "generated_data")
wavegen.plot_from_csv("generated_data.csv", 100)


## 3
# pcdr.wave_gen(100, 3, 2, "r", "generated_data")
# timestamps, y_vals = pcdr.parse_csv("generated_data.csv", 100)
# plt.plot(timestamps, y_vals, "*", markersize=10)
# plt.show()


## 4  (challenge)
# pcdr.wave_gen(100, 3, 2, "r", "generated_data_part_a")
# pcdr.wave_gen(100, 1, 4, "r", "generated_data_part_b")
# times_a, part_a = pcdr.parse_csv("generated_data_part_a.csv", 100)
# times_b, part_b = pcdr.parse_csv("generated_data_part_b.csv", 100)
# data_together = np.concatenate([part_a, part_b])
# plt.plot(data_together, "*", markersize=10)
# plt.show()
```