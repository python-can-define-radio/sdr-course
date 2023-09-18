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


## 2. 
## Try this.
## Notice that the wave degrades at higher frequencies.
from pcdr import makeRealWave_time
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))  # since we have multiple subplots this makes it large enough so nothing gets cropped off

samp_rate = 20
seconds = 2

freq = 1
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(221, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 3
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(222, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 6
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(223, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 9
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
plt.subplot(224, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

plt.tight_layout()
plt.show()


## 3
## Copy and modify the previous example (including the code for all
## of the subplots). Set the samp_rate to 40.
## Do the waves appear to be higher or lower quality?
```

As you can see, a higher sample rate allows you to measure a broader range of frequencies because it raises the threshold at which degradation begins.

Now, let's look at what happens when the frequency is very close to the sample rate. _Note: You'll notice that we have to specify `allowAliasing=True`. Normally, the `makeRealWave_time` function will prevent you from making the mistake of using too high of a frequency. In this case, we disable that safeguard so that we can demonstrate aliasing._

```python3
## 4
## Try this. Notice that the frequency is 39,
## but when you plot it, it (surprisingly) has a frequency of 1.
## What is the name for this phenomenon? 
samp_rate = 40
seconds = 2
freq = 39
timestamps, wave = makeRealWave_time(seconds, samp_rate, freq, allowAliasing=True)
plt.title(f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")
plt.show()
```

The above exercise shows **aliasing**. (You can review the explanation of aliasing [here](https://gallicchio.github.io/learnSDR/lesson06.html)).

```python3
## 5
## Copy and modify the previous example.
## Set the freq to 37.
## Due to aliasing, what frequency is displayed?
```

### Aliasing demonstration using gqrx

Aliasing in signal processing happens when you measure a signal that is outside of what your sample rate allows.

1. Open GQRX on the instructor screen. Tune to the broadcast FM range.
2. Have a student run the noise jammer, tuned to near the top end of the spectrum.
3. Slowly raise the noise jammer past the right edge. It will incorrectly appear on the left edge due to aliasing.
 
### How to fix?

In the FM Radio flowgraph, we use the "filteron" checkbox to do analog filtering inside the Hack RF.

In GQRX, you should be able to use the same filter, but as far as I can tell, there's a bug that prevents that from working, unfortunately. (Either that, or I'm doing it wrong.)
