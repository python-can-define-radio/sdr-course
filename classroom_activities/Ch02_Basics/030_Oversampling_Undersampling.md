<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 08: 050-Nyquist.md
2022 Aug 30: 090-Nyquist.md 
2023 Jan 04: 082-Nyquist.md 
2023 Jan 23: 082LATER-Nyquist.md 
2023 Jan 28: 999-Nyquist.md
2023 May 22: 040_Nyquist.md
2023 Aug 23: 030_Oversampling_Undersampling.md
</pre>
</details>

# Oversampling and Undersampling

ℹ️ This material coincides with material from SDR slideshow A (slides 22, 25, 28-32, 40-42).

### Sampling (specifically undersampling and why it's a problem)

Start by reading this [Sampling lesson on this page from Harvey Mudd](https://gallicchio.github.io/learnSDR/lesson06.html).

_Note: at time of writing, the caption is wrong on Figure 3. However, the page correctly explains what is happening._

If you'd like to read further, see also [this page from allaboutcircuits.com](https://www.allaboutcircuits.com/technical-articles/nyquist-shannon-theorem-understanding-sampled-systems/).

### Nyquist and Aliasing

_Nyquist: [Helicopter blade demonstration of Nyquist theorem](https://www.youtube.com/watch?v=yr3ngmRuGUc)_

ℹ️ Prerequisite: `pip install pcdr`


```python3
## 1.
## What figure in the Harvey Mudd page demonstrates what is happening in this video? 


## 2a 
## Try this.
## Notice that the wave degrades the closer the frequency gets to the sample rate.
from pcdr import makeRealWave_time
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))  # since we have multiple subplots this makes it large enough so nothing gets cropped off

samp_rate = 20
seconds = 2

freq = 1
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 1, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 3
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 2, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 6
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 3, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 9
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 4, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

plt.tight_layout()
plt.show()


## 2b
## This time instead of varying the frequency we see the same degradation with a varying sample rate as it approaches the value of the frequency.
from pcdr import makeRealWave_time
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))  # since we have multiple subplots this makes it large enough so nothing gets cropped off

freq = 5
seconds = 2

samp_rate = 25
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 1, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

samp_rate = 20
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 2, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

samp_rate = 15
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 3, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

samp_rate = 10
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(2, 2, 4, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

plt.tight_layout()
plt.show()


## 3
## Copy and modify the 2a example (including the code for all
## of the subplots). Set the samp_rate to 40.
## Do the waves appear to be higher or lower quality?
```

As you can see, a higher sample rate allows you to measure a broader range of frequencies because it raises the threshold at which degradation begins.

Now, let's look at what happens when the frequency is very close to the sample rate. _Note: You'll notice that we have to specify `allowAliasing=True`. Normally, the `makeRealWave_time` function will prevent you from making the mistake of using too high of a frequency. In this case, we disable that safeguard so that we can demonstrate aliasing._

```python3
## 4a
## Try this. Notice that the frequency is 9,
## but when you plot it, it (surprisingly) has a frequency of 1.
## What is the name for this phenomenon? 
from pcdr import makeRealWave_time

samp_rate = 10
seconds = 1
freq = 9
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq, allowAliasing=True)
plt.title(f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")
plt.show()


## 4b
## Let's view that with an adequate sample rate at the same time to see the difference.
from pcdr import makeRealWave_time

seconds = 1
samp_rate_too_low = 10
samp_rate_adequate = 400
freq = 9
timestamps, wave = makeRealWave_time(seconds, samp_rate_too_low, freq, allowAliasing=True)
timestamps2, wave2 = makeRealWave_time(seconds, samp_rate_adequate, freq)

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(timestamps, wave, "o-", label=f"{freq} Hz with {samp_rate_too_low} Sps")
plt.plot(timestamps2, wave2, "x-", label=f"{freq} Hz with {samp_rate_adequate} Sps")
plt.legend(loc="upper right")
plt.show()
```

The above exercise shows [**aliasing**](https://gallicchio.github.io/learnSDR/lesson06.html).

```python3
## 5
## Copy and modify the above example.
## Set the freq to 37 and the sample_rate_too_low variable to 40.
## Due to aliasing, what frequency is displayed by the blue line?
## What is the relationship between the displayed frequency and the sample rate?
```

When the frequency is above the Nyquist limit (half the sample rate), aliasing will cause the displayed frequency to appear to be a different frequency. The aliased frequency will always be the difference between the actual frequency and the sample rate.
  
|  Frequency | Sample Rate | Displayed Frequency |
|-----|-----|-----|
| 39 Hz | 40 sps | 1 Hz |
| 37 Hz | 40 sps | 3 Hz |
| 30 Hz | 40 sps | 10 Hz |

### Aliasing demonstration using gqrx

Aliasing in signal processing happens when you measure a signal that is outside of what your sample rate allows.

1. Open GQRX on the instructor screen. Tune to the broadcast FM range.
2. Have a student run the noise jammer, tuned to near the top end of the spectrum.
3. Slowly raise the noise jammer past the right edge. It will incorrectly appear on the left edge due to aliasing.
 
### How to fix?

In the FM Radio flowgraph, we use the "filteron" checkbox to do analog filtering inside the Hack RF.

In GQRX, you should be able to use the same filter, but as far as I can tell, there's a bug that prevents that from working, unfortunately. (Either that, or I'm doing it wrong.)
