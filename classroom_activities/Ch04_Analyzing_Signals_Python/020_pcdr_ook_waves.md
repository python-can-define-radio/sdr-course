## Wave theory

ℹ️ This material coincides with material from python slideshows B (slides 1-11, 16, 24, 39, 54-63, 69) C (slides 30-38) and D (slides 4-15, 31-37), and SDR slideshow A (slides 22, 25, 28-32, 40-42).

We've sent some OOK-modulated data. Now, let's graph that data and explore it.

### Graphing simple waves

We'll start by exploring two functions from the `pcdr` package that create waves: `makeRealWave_time` and `makeRealWave_numsamps`.

Unless stated otherwise in these lessons, the unit for time will be seconds rather than milliseconds or microseconds.
The unit of frequency is Hertz or Hz, which is equivalent to 1/sec.  Actually, the numerator may be assigned a unit too, so Hz may also be described as cycles per second.

```python3
## 1a
## Try this.
## Notice that you only see two cycles. Why?
## With the help of your editor, determine
##  what the `100` and the `4` represent.
import matplotlib.pyplot as plt
from pcdr import makeWave

timestamps, wave = makeWave(100, 4, "real", seconds=0.5)
plt.plot(timestamps, wave, "*", markersize=10)
plt.show()


## 1b
## Try this.
## How much time is displayed?
## How is that related to the number of samples and the sample rate?
import matplotlib.pyplot as plt
from pcdr import makeWave

timestamps, wave = makeWave(200, 4, "real", num=100)
plt.plot(timestamps, wave, "*", markersize=10)
plt.show()


## 2
## Plot a wave that completes two cycles in 1 second
## using the makeWave function.
## Complete this exercise by specifying `seconds`,
## then do it again by specifying `num`.


## 3
## Plot a wave that completes a cycle in two seconds
## using the makeWave function.


## 4a
## Ask the user for
## - The frequency of the wave to plot
## - The sample rate
## - The amount of time (that is, the number of seconds)
## - (Optional) the markersize
## - (Optional) the marker (currently "*". Valid choices are listed in the matplotlib docs. You can also experiment.)

## 4b
## Same as the previous exercise, but this time, ask the user for
## - The frequency of the wave to plot
## - The number of samples
## - The amount of time (that is, the number of seconds).
## You'll need to compute the sample rate from the given information.
```

### Revisiting OOK

Now that we've plotted a wave, let's look back at our `ook_modulate` function.

```python3
## 5
## Try this.
import matplotlib.pyplot as plt
from pcdr import ook_modulate

modulated = ook_modulate([1, 0, 1, 0], bit_length=4)
plt.plot(modulated, "*-", markersize=20)
plt.show()


## 6
## Copy and modify the above example so that each bit is 10 samples long.
```

You may be surprised that the `ook_modulate` function doesn't produce a wave. Why were we able to send this data to the Hack RF when it doesn't seem to have a carrier wave? Remember that when working with the Hack RF in GNU Radio Companion, we specify a center frequency (or "Ch0 Frequency"). For any data that you ask it to send, the Hack RF first shifts the data to the specified center frequency. This is known as [**upconversion**](https://en.wiktionary.org/wiki/upconversion).

### OOK on a wave

There are cases in which we would like to impose the data on a carrier wave in software before the Hack RF does its own shift. For example, you may wish to transmit on two different frequencies simultaneously. We'll do that at somepoint, but let's try a more basic upconversion example first:

```python3
## 7
## Try this.
import matplotlib.pyplot as plt
from pcdr import makeRealWave_numsamps, ook_modulate

modulated = ook_modulate([1, 0, 1, 0], bit_length=25)
timestamps, wave = makeRealWave_numsamps(num_samples=100, samp_rate=100, freq=4)
upconverted = modulated * wave
plt.plot(timestamps, upconverted, "*-", markersize=10)
plt.show()


## 8
## Try this.
import matplotlib.pyplot as plt
from pcdr import makeRealWave_numsamps, ook_modulate

modulated = ook_modulate([1, 0, 1, 0], bit_length=50)
timestamps, wave = makeRealWave_numsamps(num_samples=200, samp_rate=100, freq=4)
upconverted = modulated * wave
plt.plot(timestamps, upconverted, "*-", markersize=10)
plt.show()
```

Notice that in both of these examples, the data more closely resembles the classic OOK picture: wave turns on, wave turns off.

The key line is `upconverted = modulated * wave`. This multiplies each point in `wave` by each point in `modulated`. Remember that `modulated` is an array of only ones and zeros. Multiplying by one does not change a number, and multiplying by zero results in zero.

Also notice that when we set the `num_samples` to `200`, we had to change the `bit_length` to `50`. The reason: the length of `modulated` is going to be the number-of-bits times the `bit_length`, which in this case is `4 * 50 = 200`. That length must match the length of `wave` because we are multiplying them point-by-point. The length of `wave` is always equal to the length of `timestamps`, which is based on `num_samples`.

Let's practice.

```python3
## 9
## Copy and modify the previous example. Change the bit_length to 100.
## You'll also need to adjust num_samples. What should it be?


## 10
## Copy and modify the previous example. Change the data to [1, 0, 1, 1, 0].
## You'll also need to adjust num_samples. To decide how, think about how long your
## data is after running ook_modulate.
```

Manually updating `num_samples` based on the length of your data is somewhat tedious and error-prone. We can ask the computer to do that for us by setting `num_samples` to the length of `modulated`:

```python3
## 11
## Try this.
modulated = ook_modulate([1, 0, 0, 1, 0, 1], bit_length=25)
timestamps, wave = makeRealWave_numsamps(num_samples=len(modulated), samp_rate=100, freq=8)
upconverted = modulated * wave
plt.plot(timestamps, upconverted, "*-", markersize=10)
plt.show()
```

Now, since `num_samples` is set to the length of our modulated data, we can freely change the `bit_length` or the content of `data`, and the length of `wave` will automatically adjust.

### Cycles per bit

Notice that in the previous example, there are two cycles of the wave for a single bit. In the next example, we'll see four cycles per bit.

```python3
## 12
## Copy and modify the previous example. Change the freq to 16.
## Is the 100101 pattern still distinguishable?


## 13
## Copy and modify the previous example. Change the freq to 5.
## Is the 100101 pattern still distinguishable?
```

As you can see from the previous examples, the number of cycles-per-bit is arbitrary. In fact, it does not need to be a whole number! The information is communicated by the wave being "turned on" or "turned off".

That being said, in "real life", there are reasons to pick a certain frequency:
- Others may be transmitting on nearby frequencies. That means that the chosen frequency needs to be known by both transmitter and receiver so that the receiver can filter out unwanted transmissions.
- Different frequencies have different propagation characteristics.

### Additional Practice

Now that we know how to put bits on a wave, let's incorporate the function that converts strings to binary.

```python3
## 14
## Using the function str_to_bin_list from the previous exercise set, 
## - Ask the user for a string
## - Convert the string to a list of bits
## - OOK modulate the bits
## - Shift to a carrier frequency of 3 Hz
## - Plot the result 
```
