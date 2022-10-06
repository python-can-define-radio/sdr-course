## Introduction

_Prerequisites: `038`, `039`, `040`, `041`_

We've successfully transmitted evenly-spaced pulses using the Hack RF. The next goal is to transmit something more interesting, such as this:

```
   ___   ___   ______   ___      ___
___   ___   ___      ___   ______   ___
```

If we interpreted this as binary, it might look like this:

```
   ___   ___   ______   ___      ___
___   ___   ___      ___   ______   ___
0  1  0  1  0  1  1  0  1  0  0  1  0
```

So, can we simply swap out the Square Wave Signal Source that we saw in `041`? Yes and no. Before answering that question, we must explore how sample rates work.

## What is a Sample Rate?

### Thermometers and paper

Imagine that you're keeping a record of temperatures in your area. You have a thermometer, a piece of paper, and a pencil. You occasionally look at the thermometer and write down the current temperature.

Each measurement of the temperature is called a **sample**. The **sample rate** refers to how frequently you take a measurement.

How often would you want to sample the temperature? You could write down the temperature once every minute. In that case, the sample rate would be `1 sample per minute`, or `60 samples per hour`.

But is it really necessary to measure the temperature so frequently? Perhaps one or two samples per hour would be more reasonable, given that the ambient temperature doesn't change very much within a minute.

Let's imagine that you did one sample every two hours, or 12 samples per day. It might look like this:

```
12 am   52 °F
2 am    50 °F
4 am    48 °F
6 am    48 °F
8 am    46 °F
10 am   58 °F
12 pm   63 °F
2 pm    64 °F
4 pm    67 °F
6 pm    66 °F
8 pm    63 °F
10 pm   57 °F
```

Let's graph this in Python. For simplicity, I'm omitting the times.

Filename: `temperature_graph_1.py`

```python3
import matplotlib.pyplot as plt

temps = [52, 50, 48, 48, 46, 58, 63, 64, 67, 66, 63, 57]

plt.plot(temps, "o")    #  the "o" means to use circles as markers of the points

plt.show()
```

Now, let's graph it in GNU Radio Companion.

Filename: `temperature_graph_2.grc`

```
Vector Source  -->  Time Sink
```

Parameters:  
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `0.5`
- Vector Source:
  - Output Type: `float`
  - Vector: `[52, 50, 48, 48, 46, 58, 63, 64, 67, 66, 63, 57, 0, 0, 0]`
  - Repeat: `No`
- Time Sink:
  - General tab:
    - Type: `float`
    - Number of Points: `12`
    - Y min: `0`
    - Y max: `100`
  - Config tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`

Notes:
- The zeros at the end of the data in the Vector Source are unfortunately necessary because of a quirk in GNU Radio. My guess is that it requires the chunks of data to have some minimum length before moving the data to from block to block.
- We put a sample rate of 0.5 samples per second. It should actually be 0.5 samples per hour (meaning 1 sample every two hours), but GNU Radio is quirky with low sample rates. Pretend that the x-axis label says "hours" instead of "seconds".


# Part

# Below

# Will

# Soon

# Be

# Moved

# To 

# A

# New

# File

# The Flowgraph:

## sample_rates_one.grc

```
GUI Range

Signal Source  --->  Throttle  --->  Time Sink
                               --->  Waterfall Sink
                               --->  Frequency Sink
```

### Parameters:

- GUI Range:
  - Id: `sigfreq`
  - Default: `3`
  - Start: `1`
  - Stop: `5`
  - Step: `1`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `30`
- Signal Source:
  - Output Type: `float`
  - Waveform: `Sine`
  - Frequency: `sigfreq`
- Throttle:
  - Type: `float`
  - Sample Rate: `40000`
- Time Sink:
  - "General" Tab:
    - Type: `float`
    - Number of Points: `30`
    - Y min: `-4`
    - Y max: `4`
  - "Trigger" Tab:
    - Trigger Mode: `Normal`
  - "Config" Tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`
- Waterfall Sink:
  - Type: `Float`
  - Spectrum Width: `Half`  (_Note: This option only appears after you've picked Float for the type_)
- Frequency Sink:
  - Type: `Float`
  - Spectrum Width: `Half`
  - Y Min: `-110`


# FAQ

- Q: What does the Throttle do?  
  A: It keeps the processor from maxing out. GNU Radio tries to run the simulation as quickly as possible, that is, as quickly as the computer is capable. The Throttle tells it to slow down. Feel free to try raising or lowering the Sample Rate in the Throttle. You'll see that for lower rates (say, `200`), the slider is less responsive.
- Q: What is the difference between `Float` and `Complex`?  
  A: We'll discuss more later, but for now, know this:  
   -  Float has only one part (the real part), while Complex has two parts (real and imaginary). That means that in a Time Sink, Float will show one curve, while Complex will show two.

# Exercises

1. How many total data points are displayed in the Time Sink?
2. How many seconds are shown on the horizontal axis of the Time Sink?
3. When the frequency is 3 Hz, how many cycles do you see in the Time Sink?
4. How many data points (a.k.a. "samples") are there in a single cycle when the frequency is 3 Hz?
