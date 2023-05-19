## Intro: OOK Revisited

As you may recall from `050`, On-Off Keying (OOK) involves turning something (such as a wireless signal) on and off.

In the last few exercises, we've managed to make the on-off signal. Now, we need to impose that on a wave (as shown [here](https://www.open.edu/openlearn/science-maths-technology/exploring-communications-technology/content-section-1.4)), so we can send it to the Hack RF.

<details><summary><i>Do we actually need to?</i></summary>

Strictly speaking, you could send the data into an osmocom Sink without making it into a wave. However, this approach helps us to make a more complete simulation of what's happening behind the scenes before we switch to using real hardware. Ask an instructor if you're interested.

</details>

## Square Pulses and Sine Waves 

What math operation should we use to combine the on-off pulses with a sine wave? Let's experiment.

We're going to graph an on-off signal (a square wave) and a sine wave. Feel free to try it on paper first:

The square wave will be plotted from `0 seconds` to `2 seconds`, and will have these attributes:

- When the wave is high, it is `1`.
- When the wave is low, it is `0`.
- The wave starts low.
- One full cycle (the **period**) is `1 second`.
- Question: What is the frequency?

We'll also graph a Sin wave with a frequency of `4 Hz` across the same time range.

Here's the Python code to graph it. Name this `square_and_sine_1.py`.

```python3
import matplotlib.pyplot as plt
import numpy as np

x_axis_label = np.linspace(0, 1.99, 200)
sqr = np.concatenate([np.zeros(50), np.ones(50), np.zeros(50), np.ones(50)])
wavey = np.sin(x_axis_label * 4 * 2 * np.pi)

plt.plot(x_axis_label, sqr, "o")
plt.plot(x_axis_label, wavey, "o")

plt.show()
```

Then, let's look at the two multiplied:

```python3
plt.plot(x_axis_label, sqr * wavey, "o")
plt.show()
```

In the next exercise, we'll use GNU Radio Companion to do the same thing.
