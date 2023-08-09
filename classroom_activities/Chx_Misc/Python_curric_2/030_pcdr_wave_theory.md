## Wave theory

We've sent some OOK-modulated data. Now, let's graph that data and explore it.

We'll start by simply graphing a wave.

```python3
## 1
## Try this.
import matplotlib.pyplot as plt
from pcdr.wavegen import createTimestamps, makeRealWave

timestamps = createTimestamps(seconds=1.0, num_samples=100)
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

You may be surprised that the `ook_modulate` function doesn't produce a wave. Why were we able to send this data to the Hack RF when it doesn't seem to have a carrier wave? Remember that when working with the Hack RF in GNU Radio Companion, we specify a center frequency (or "Ch0 Frequency"). For any data that you ask it to send, the Hack RF first shifts the data to the specified center frequency. This is known as **upconversion**.

There are cases in which we would like to impose the data on a carrier wave in software before the Hack RF does its own shift. Let's try it:

```python3
## 7
## Try this.
import matplotlib.pyplot as plt
from pcdr.wavegen import createTimestamps, makeRealWave
from pcdr.modulators import ook_modulate

timestamps = createTimestamps(seconds=1.0, num_samples=100)
wave = makeRealWave(timestamps, freq=4)
modded = ook_modulate(data=[1, 0, 1, 0], bit_length=25)
fully_modded = modded * wave
plt.plot(timestamps, fully_modded, "*-", markersize=20)
plt.show()
```

Notice that the data more closely resembles the classic OOK picture: wave turns on, wave turns off.

The key line is `fully_modded = modded * wave`. This multiplies each point in `wave` by each point in `modded`. Remember that `wave` is an array of only ones and zeros. Multiplying by one does not change a number, and multiplying by zero results in zero.

```python3
## 8
## Copy and modify the previous example. Change the data to [1, 0, 1, 1, 0].
## You'll also need to adjust num_samples. To decide how, think about how long your
## data is after running ook_modulate.
```

In the most recent exercise, you needed to update `num_samples` based on the length of your data. We can ask the computer to do that for us by setting `num_samples` to the length of `modded`:

```python3
## 9
## Try this.
modded = ook_modulate(data=[1, 0, 0, 1, 0, 1], bit_length=25)
timestamps = createTimestamps(seconds=1.0, num_samples=len(modded))
wave = makeRealWave(timestamps, freq=4)
fully_modded = modded * wave
plt.plot(timestamps, fully_modded, "*-", markersize=20)
plt.show()


## 10
## Using the function str_to_bin_list from the previous exercise set, 
## - Ask the user for a string
## - Convert the string to a list of bits
## - OOK modulate the bits
## - Plot the result 
```


```python3
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
