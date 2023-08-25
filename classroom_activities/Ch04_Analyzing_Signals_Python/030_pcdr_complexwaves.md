# Complex waves

In the previous lesson, all of the waves that we generated and plotted were real waves. In other words, they had only a real component, and no imaginary component. This lesson will introduce complex waves, which are those that have both a real and an imaginary component. In an SDR context, these are often called IQ signals, which means In-phase (I) and Quadrature (Q). The I refers to  the real part, and the Q refers to the imaginary part.

### Why are we working with imaginary numbers?

The math behind SDRs (and, consequently, the software used with SDRs) is based on complex numbers. This has a few advantages. One such advantage:  
**Complex numbers allow for a representation of both positive and negative frequencies.**

### Negative Frequencies

Often, when beginning to work with SDRs, people ask, "What is a negative frequency?" The question is reasonable, as it seems that if something is shaking twice per second, it doesn't matter which direction it's shaking — it's simply shaking twice per second.

The PySDR website has a [useful diagram](https://pysdr.org/content/frequency_domain.html#negative-frequencies) for this. You'll see that their SDR's center frequency is tuned to 100 MHz. When the HackRF One gives the signal to the computer via the USB cable, the signals will have been **downconverted**. That means...

- The "yellow trapezoid" signal, which was ≈ 104 MHz, will be downconverted to ≈ +4 MHz.
- The "green trapezoid" signal, which was ≈ 100 MHz, will be downconverted to ≈ 0 MHz.
- The "blue triangle" signal, which was ≈ 97.5 MHz, will be downconverted to ≈ -2.5 MHz.

Notice that all three frequencies are still represented, even though one is now negative. They are now shifted to near zero based on where they were in relation to your tuned frequency.

So, how do you represent a negative frequency? Let's demonstrate that in a plot using Python.

```python3
## 1 
## Try this.
import matplotlib.pyplot as plt
from pcdr import makeComplexWave_time



timestamps, wave = makeComplexWave_time(seconds=2, samp_rate=50, freq=2)
plt.subplot(211, title="Frequency = +2 Hz")
plt.plot(timestamps, wave.real, "^-", color="blue", label="Real")
plt.plot(timestamps, wave.imag, "*-", color="red", label="Imag")
plt.legend(loc="upper right")

timestamps, wave = makeComplexWave_time(seconds=2, samp_rate=50, freq=-2)
plt.subplot(212, title="Frequency = -2 Hz")
plt.plot(timestamps, wave.real, "^-", color="blue", label="Real")
plt.plot(timestamps, wave.imag, "*-", color="red", label="Imag")
plt.legend(loc="upper right")

plt.tight_layout()
plt.show()
```

Can you see a difference between the two plots?
<details><summary><i>Click here for answer...</i></summary>
  
- For the wave with positive frequency, the real (blue) part is one-quarter-cycle BEFORE the imaginary (red) part.
- For the wave with negative frequency, the real (blue) part is one-quarter-cycle AFTER the imaginary (red) part.
  
</details>

If you'd like to delve into the underlying concepts, Arachnoid.com provides a [great explanation](https://arachnoid.com/software_defined_radios/) (along with a [really cool interactive Javascript applet](https://arachnoid.com/software_defined_radios/#Theory__I_Q_Exploration_Applet)) for exploring IQ signals. 

Let's get some more practice working with complex waves.

```python3
## 2
## Use the makeComplexWave_time function to make a wave with frequency 3 Hz.
## Plot the wave from 0 to 4 seconds.


## 3
## Use the makeComplexWave_time function to make a wave with frequency 0.5 Hz.
## Plot the wave from 0 to 2 seconds. 
```

### Adding waves

When the signal is made up of a single wave, we can fairly easily identify the frequency of that wave. Even if there are two frequencies present, it's not too difficult to distinguish the frequencies that are present:

```python3
## 4
## Try this example, which plots a 2 Hz wave and a 15 Hz wave.
## Notice that we're only plotting the sum of the waves.
## Can you still distinguish the two separate frequencies?
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time

seconds = 2
samp_rate = 500
timestamps, wave1 = makeRealWave_time(seconds=seconds, samp_rate=samp_rate, freq=2)
timestamps, wave2 = makeRealWave_time(seconds=seconds, samp_rate=samp_rate, freq=15)
added = wave1 + wave2
plt.plot(timestamps, added, "*-", markersize=5)
plt.show()


## 5
## Copy and modify the previous example.
## Change the first wave's frequency to 3 Hz.
## Can you still distinguish the two waves?


## 6
## Copy and modify the previous example.
## Change the first wave's frequency to 11 Hz.
## Notice that distinguishing the two waves is more difficult.
```

We've been looking at the **Time Domain** view of the wave. In other words, we're viewing the measured samples over a period of time. As you saw in the most recent example, there can be difficulties distinguishishing the frequencies that are present.

### The frequency domain

The solution to the limitations of the Time Domain is to view the signal in the **Frequency Domain**. Here's an example:

```python3
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time, make_fft_positive_freqs_only

maxTime = 2
samp_rate = 500
timestamps, wave1 = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=2)
timestamps, wave2 = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=15)
added = wave1 + wave2
sample_freqs, fft_mag = make_fft_positive_freqs_only(added, samp_rate)
plt.subplot(2, 1, 1, title="Time Domain")
plt.plot(timestamps, added, "*-", markersize=5)
plt.subplot(2, 1, 2, title="Frequency Domain")
plt.plot(sample_freqs, fft_mag, '.r-')
plt.tightlayout()
plt.show()
```

TODO: DISCUSS