# Frequency Domain and Real Waves

ℹ️ This material coincides with material from python slideshows B (slides 1-11, 16, 24, 39, 54-63, 69) C (slides 30-38) and  D (slides 4-15, 31-37).

### Adding waves

When the signal is made up of a single wave, we can fairly easily identify the frequency of that wave. Even if there are two frequencies present, it's not too difficult to distinguish the frequencies that are present:

```python3
## 1
## Try this example, which plots a 2 Hz wave and a 25 Hz wave.
## Notice that we're only plotting the sum of the waves.
## Can you still distinguish the two separate frequencies?
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time

seconds = 2
samp_rate = 300
timestamps, wave1 = makeRealWave_time(seconds=seconds, samp_rate=samp_rate, freq=2)
timestamps, wave2 = makeRealWave_time(seconds=seconds, samp_rate=samp_rate, freq=25)
added = wave1 + wave2
plt.plot(timestamps, added, "*-", markersize=5)
plt.show()


## 2
## Copy and modify the previous example.
## Change the first wave's frequency to 3 Hz.
## Can you still distinguish the two waves?


## 3
## Copy and modify the previous example.
## Change the first wave's frequency to 11 Hz.
## Notice that distinguishing the two waves is more difficult.
```

We've been looking at the **Time Domain** view of the wave. In other words, we're viewing the measured samples over a period of time. As you saw in the most recent example, there can be difficulties distinguishishing the frequencies that are present.

### The frequency domain

The solution to the limitations of the Time Domain is to view the signal in the **Frequency Domain**. Here's an example:

```python3
## 4
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time, make_fft_positive_freqs_only

maxTime = 2
samp_rate = 300
timestamps, wave = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=10)
sample_freqs, fft_mag = make_fft_positive_freqs_only(wave, samp_rate)
plt.subplot(2, 1, 1, title="Time Domain")
plt.plot(timestamps, wave, "*-", markersize=5)
plt.subplot(2, 1, 2, title="Frequency Domain")
plt.plot(sample_freqs, fft_mag, '.g-')
plt.show()
```

In the window that opens, you'll see two subplots, labeled "Time Domain" and "Frequency Domain". Notice that there is a spike in the Frequency Domain at 10 Hz to indicate the frequency that is present in this signal.

```python3
## 5
## Plot the time domain and the frequency domain for
## a (real) sine wave with frequency = 4 Hz.
```

Let's try it with two signals added:

```python3
## 6
## Try this.
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time, make_fft_positive_freqs_only

maxTime = 2
samp_rate = 300
timestamps, wave1 = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=2)
timestamps, wave2 = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=25)
added = wave1 + wave2
sample_freqs, fft_mag = make_fft_positive_freqs_only(added, samp_rate)
plt.subplot(2, 1, 1, title="Time Domain")
plt.plot(timestamps, added, "*-", markersize=5)
plt.subplot(2, 1, 2, title="Frequency Domain")
plt.plot(sample_freqs, fft_mag, '.g-')
plt.tight_layout()
plt.show()
```

In this example, the Frequency Domain has two spikes, located at 2 Hz and 25 Hz.

```python3
## 7
## Copy and modify the previous example.
## Change this line:
##     added = wave1 + wave2
## ...to this:
###    added = wave1 + (0.5*wave2)
```

Notice that with the `0.5` modification, the amplitude of the 25 Hz wave is now half of the amplitude of the 2 Hz wave.

Also notice that this change is visible in both the time domain and the frequency domain, but it is much more obvious in the frequency domain.

For the next exercise, you may wish to refer to the [matplotlib subplot command documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html).

```python3
## 8
## Copy modify the previous example so that it has four subplots:
##  - The original wave (wave1 + wave2), displayed in the time domain
##  - The original wave (wave1 + wave2), displayed in the frequency domain
##  - The new wave (wave1 + (0.5*wave2)), displayed in the time domain
##  - The new wave (wave1 + (0.5*wave2)), displayed in the frequency domain
## You may wish to consult the matplotlib subplot documentation listed above.
```

### The Dark Side of the Frequency Domain (Negative Frequencies)

Up to this point, we've been using the function `make_fft_positive_freqs_only`. The name begs the question -- why are we only looking at only positive frequencies? What happens if you use `make_fft` instead? Let's try it.

```python3
## 9
## Try this.
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time, make_fft

maxTime = 2
samp_rate = 300
timestamps, wave1 = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=2)
timestamps, wave2 = makeRealWave_time(seconds=maxTime, samp_rate=samp_rate, freq=25)
added = wave1 + (0.5*wave2)
sample_freqs, fft_mag = make_fft(added, samp_rate)
plt.subplot(2, 1, 1, title="Time Domain")
plt.plot(timestamps, added, "*-", markersize=5)
plt.subplot(2, 1, 2, title="Frequency Domain")
plt.plot(sample_freqs, fft_mag, '.g-', markersize=4)
plt.tight_layout()
plt.show()
```

Notice in the frequency domain that there are now four spikes: -25 Hz, -2 Hz, +2 Hz, +25 Hz.

Let's try a different signal:

```python3
## 10
## Copy and modify the previous example. Change both frequencies.
```

You'll notice that no matter what frequencies you pick, the Frequency Domain will always be symmetric.

You may wonder: why we would ever display the negative frequencies if they'll always be the same as their positive counterparts? The answer: for real signals, the Frequency Domain will always be symmetric, but for signals that are not purely real, they won't necessarily be symmetric.

_A non-real signal? What does that mean?_ See the next lesson for the answer!

A good video showing how the position of a circle corresponds to the values on a sine wave.  
[sine_wave_video](https://www.youtube.com/watch?v=k8FXF1KjzY0&t=4s)

