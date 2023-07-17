<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 30: 030-Sample-Rates-1.md
2022 Sep 15: 050-Sample-Rates-1.md
2023 May 22: 020_Sample_Rates_Intro-1.md
</pre>
</details>

## Introduction

At this point, you've used various Graphical User Interface (GUI) features to manually adjust the amplitude and the frequency of a pure sine wave. Human-powered modulation is certainly useful, as thousands of telegraph operators could tell you.

But as we know, the telegraph has fallen out of style. Why? Because we now have computers that can do the moduation for us.

### What is Modulation?

Strictly speaking, to "modulate" something simply means to change it. But in the context of communications, modulation refers to making a change in something (amplitude, frequency, etc) for the purpose of communicating information.

Imagine you want to communicate the following binary data using a flashlight.

```
0   1   0   1   0   1   1   0   1   0   0   1   0
```

You may choose to alternate between turning the light on and off:

```
off on  off on  off on  on  off on  off off on  off
0   1   0   1   0   1   1   0   1   0   0   1   0
```

If you were to look at a graph of the brightness over time, it would look like this:

```
    ____    ____    ________    ____        ____
____    ____    ____        ____    ________    ____
0   1   0   1   0   1   1   0   1   0   0   1   0
```

The name for this modulation scheme is "On Off Keying".  The website _Open Learn_ has a [great figure for visualizing On Off Keying](https://www.open.edu/openlearn/science-maths-technology/exploring-communications-technology/content-section-1.4)

So, how do we make the Hack RF transmit and receive OOK modulated data? To answer that question, we'll be taking a long detour to explore how sample rates work.

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

Open your editor of choice (for example, VS Code). Open your directory (the one you created on the Desktop) inside of VS Code. Using VS Code, create this file in that directory:

Filename: `temperature_graph_1.py`

```python3
import matplotlib.pyplot as plt

times = [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22]
temps = [52, 50, 48, 48, 46, 58, 63, 64, 67, 66, 63, 57]

font1 = {"family":"serif", "color":"blue", "size":20}
font2 = {"family":"serif", "color":"darkred", "size":15}

plt.title("Temperature Samples", fontdict=font1)
plt.xlabel("Time (Hours)", fontdict=font2)
plt.ylabel("Temperature (° F)", fontdict=font2)

plt.plot(times, temps, marker="o", linestyle="dotted")

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
  - Vector: `(52, 50, 48, 48, 46, 58, 63, 64, 67, 66, 63, 57, 0, 0, 0)`
  - Repeat: `No`
- Time Sink:
  - General tab:
    - Type: `float`
    - Y Axis Label: `Temperature`
    - Y Axis Unit: `Deg F`
    - Number of Points: `12`
    - Y min: `0`
    - Y max: `100`
  - Config tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`

Notes:
- The zeros at the end of the data in the Vector Source are unfortunately necessary because of a quirk in GNU Radio: the Time Sink won't display _any_ data unless you add a few extra data points past the 12 that it is going to show. (The value of zero is not special; any extra data works.) My guess is that it requires the chunks of data to have some minimum length before moving the data from block to block. Also, I believe those chunks must be longer than the number of points that you are viewing in the Time Sink. 
- We put a sample rate of 0.5 samples per second. It should actually be 0.5 samples per hour (meaning 1 sample every two hours), but GNU Radio is quirky with low sample rates. Pretend that the x-axis label says "hours" instead of "seconds".

