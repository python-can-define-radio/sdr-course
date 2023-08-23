## Wave theory

We've sent some OOK-modulated data. Now, let's graph that data and explore it.

### Graphing simple waves

```python3
## 1
## Try this.
import matplotlib.pyplot as plt
from pcdr import createTimestamps, makeRealWave

timestamps = createTimestamps(seconds=1.0, num_samples=100)
wave = makeRealWave(timestamps, freq=3)
plt.plot(timestamps, wave, "*", markersize=10)
plt.show()

## 2
## Copy and modify the previous example.
## Plot a wave that completes two cycles in 1 second.


## 3
## Copy and modify the previous example.
## Plot a wave that completes a cycle in two seconds.

## 4
## Ask the user for
## - The frequency of the wave to plot
## - The number of samples
## - The amount of time (that is, the number of seconds)
## - (Optional) the markersize
## - (Optional) the marker (currently "*". Valid choices are listed in the matplotlib docs. You can also experiment.)
```

### Revisiting OOK

Now that we've plotted a wave, let's look back at our `ook_modulate` function.

```python3
## 5
## Try this.
import matplotlib.pyplot as plt
from pcdr import ook_modulate

modulated = ook_modulate(data=[1, 0, 1, 0], bit_length=4)
plt.plot(modulated, "*-", markersize=20)
plt.show()


## 6
## Copy and modify the above example so that each bit is 10 samples long.
```

You may be surprised that the `ook_modulate` function doesn't produce a wave. Why were we able to send this data to the Hack RF when it doesn't seem to have a carrier wave? Remember that when working with the Hack RF in GNU Radio Companion, we specify a center frequency (or "Ch0 Frequency"). For any data that you ask it to send, the Hack RF first shifts the data to the specified center frequency. This is known as [**upconversion**](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch05_Concepts/010_UC_DC.md).

### OOK on a wave

There are cases in which we would like to impose the data on a carrier wave in software before the Hack RF does its own shift. Let's try it:

```python3
## 7
## Try this.
import matplotlib.pyplot as plt
from pcdr import createTimestamps, makeRealWave, ook_modulate

modulated = ook_modulate(data=[1, 0, 1, 0], bit_length=25)
timestamps = createTimestamps(seconds=1.0, num_samples=100)
wave = makeRealWave(timestamps, freq=8)
fully_modulated = modulated * wave
plt.plot(timestamps, fully_modulated, "*-", markersize=20)
plt.show()


## 8
## Try this.
import matplotlib.pyplot as plt
from pcdr import createTimestamps, makeRealWave, ook_modulate

modulated = ook_modulate(data=[1, 0, 1, 0], bit_length=50)
timestamps = createTimestamps(seconds=1.0, num_samples=200)
wave = makeRealWave(timestamps, freq=8)
fully_modulated = modulated * wave
plt.plot(timestamps, fully_modulated, "*-", markersize=20)
plt.show()
```

Notice that in both of these examples, the data more closely resembles the classic OOK picture: wave turns on, wave turns off.

The key line is `fully_modulated = modulated * wave`. This multiplies each point in `wave` by each point in `modulated`. Remember that `modulated` is an array of only ones and zeros. Multiplying by one does not change a number, and multiplying by zero results in zero.

Also notice that when we set the `num_samples` to `200`, we had to change the `bit_length` to `50`. The reason: the length of `modulated` is going to be `len(data) * bit_length`, which in this case is `4 * 50 = 200`. That length must match the length of `wave` because we are multiplying them point-by-point. The length of `wave` is always equal to the length of `timestamps`, which is based on `num_samples`.

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
modulated = ook_modulate(data=[1, 0, 0, 1, 0, 1], bit_length=25)
timestamps = createTimestamps(seconds=1.0, num_samples=len(modulated))
wave = makeRealWave(timestamps, freq=6)
fully_modulated = modulated * wave
plt.plot(timestamps, fully_modulated, "*-", markersize=20)
plt.show()
```

Now, since `num_samples` is set to the length of our modulated data, we can freely change the `bit_length` or the content of `data`, and the length of `wave` will automatically adjust.

### Cycles per bit

Notice that there are two cycles of the wave for a single bit. In the next example, we'll see four cycles per bit.

```python3
## 12
## Copy and modify the previous example. Change the freq to 16.
## Is the 1010 pattern still distinguishable?


## 13
## Copy and modify the previous example. Change the freq to 5.
## Is the 1010 pattern still distinguishable?
```

As you can see from the previous examples, the number of cycles-per-bit is arbitrary. In fact, it does not need to be a whole number! The information is communicated by the wave being "turned on" or "turned off".

That being said, in "real life", there are reasons to pick a certain frequency:
- Others may be transmitting on nearby frequencies. That means that the chosen frequency needs to be known by both transmitter and receiver so that the receiver can filter out unwanted transmissions.
- Different frequencies have different propagation characteristics.

### Sample Rates

Up to this point, we've been using a fixed amount of time: 1 second. However, we eventually want to transmit this data to the Hack RF, and in that context, we will have a fixed **sample rate**, not a fixed amount of time.

Here's how we handle that:

```python3
## 14
## Try this.
samp_rate = 50
modulated = ook_modulate(data=[1, 0, 0, 1, 0, 1], bit_length=25)
t = len(modulated) / samp_rate
timestamps = createTimestamps(seconds=t, num_samples=len(modulated))
wave = makeRealWave(timestamps, freq=4)
fully_modulated = modulated * wave
plt.plot(timestamps, fully_modulated, "*-", markersize=20)
plt.show()
```

Notice that `seconds` is now set to `len(modulated) / samp_rate`, which in this case equals `150 / 50`, or `3`. As a result, in the graph, there are 3 seconds of data. Reason: there are 6 bits, each of which is 25 samples long. That's 150 samples. We are working with 50 samples per second (chosen arbitrarily). Each group of 50 samples takes 1 second, so 150 samples takes 3 seconds.

```python3
## 15
## Copy and modify the previous example.
## Make the bit length 50, and make the data [1, 0, 1, 0, 1].
## How many seconds of data is this?
```

### Modulating text

Now, let's modulate some text:

```python3
## 16
## Using the function str_to_bin_list from the previous exercise set, 
## - Ask the user for a string
## - Convert the string to a list of bits
## - OOK modulate the bits
## - Plot the result 
```
