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

ℹ️ Prerequisite: `pip install --upgrade pcdr`


```python3
## 1.
## What figure in the Harvey Mudd page demonstrates what is happening in this video? 


## 2a 
## Try this.
## Notice that the wave degrades the closer the frequency gets to the sample rate.
from pcdr import makeWave
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))  # since we have multiple subplots, this makes the figure large enough that nothing gets cropped off

samp_rate = 20
seconds = 2

freq = 1
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 1, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 3
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 2, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 6
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 3, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

freq = 9
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 4, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

plt.tight_layout()
plt.show()


## 2b
## This time instead of varying the frequency we see the same degradation with a varying sample rate
## as it approaches the value of the frequency.
from pcdr import makeWave
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))  # since we have multiple subplots this makes it large enough so nothing gets cropped off

freq = 5
seconds = 2

samp_rate = 25
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 1, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

samp_rate = 20
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 2, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

samp_rate = 15
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
plt.subplot(2, 2, 3, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")

samp_rate = 10
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds)
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

Now, let's look at what happens when the frequency is very close to the sample rate. _Note: You'll notice that we have to specify `allowAliasing=True`. Normally, the `makeWave` function will prevent you from making the mistake of using too high of a frequency. In this case, we disable that safeguard so that we can demonstrate aliasing._

```python3
## 4a
## Try this. Notice that the frequency is 9,
## but when you plot it, it (surprisingly) has a frequency of 1.
## What is the name for this phenomenon? 
from pcdr import makeWave
import matplotlib.pyplot as plt

samp_rate = 10
seconds = 1
freq = 9
timestamps, wave = makeWave(samp_rate, freq, "real", seconds=seconds, allowAliasing=True)
plt.title(f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
plt.plot(timestamps, wave, "o-")
plt.show()


## 4b
## Let's view that with an adequate sample rate at the same time to see the difference.
from pcdr import makeWave
import matplotlib.pyplot as plt

seconds = 1
samp_rate_too_low = 10
samp_rate_adequate = 400
freq = 9
timestamps, wave = makeWave(samp_rate_too_low, freq, "real", seconds=seconds, allowAliasing=True)
timestamps2, wave2 = makeWave(samp_rate_adequate, freq, "real", seconds=seconds)

plt.title('As you can see, the blue line is not showing the correct frequency')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(timestamps, wave, "o-", label=f"{freq} Hz with {samp_rate_too_low} Sps")
plt.plot(timestamps2, wave2, "-", label=f"{freq} Hz with {samp_rate_adequate} Sps")
plt.legend(loc="upper right")
plt.show()
```

The above exercise shows [**aliasing**](https://gallicchio.github.io/learnSDR/lesson06.html).

```python3
## 5
## Try this.
## Due to aliasing, what frequency is displayed by the blue line?
from pcdr import makeWave
import matplotlib.pyplot as plt

seconds = 1
samp_rate_too_low = 20
samp_rate_adequate = 400
freq = 18
timestamps, wave = makeWave(samp_rate_too_low, freq, "real", seconds=seconds, allowAliasing=True)
timestamps2, wave2 = makeWave(samp_rate_adequate, freq, "real", seconds=seconds)

plt.title('The frequency displayed will be the difference\n between the frequency and the sample rate')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(timestamps, wave, "o-", label=f"{freq} Hz with {samp_rate_too_low} Sps")
plt.plot(timestamps2, wave2, "-", label=f"{freq} Hz with {samp_rate_adequate} Sps")
plt.legend(loc="upper right")
plt.show()


## 6
## Copy and modify the previous example
## Make your frequency 37 Hz and your samp_rate_too_low 40 Sps
## What is the relationship between the displayed frequency and the sample rate?
```

When the frequency is above the Nyquist limit (half the sample rate), aliasing will cause the displayed frequency to appear to be a different frequency. The aliased frequency will always be the difference between the actual frequency and the sample rate.
  
|  Frequency | Sample Rate | Displayed Frequency |
|-----|-----|-----|
| 39 Hz | 40 sps | 1 Hz |
| 37 Hz | 40 sps | 3 Hz |
| 30 Hz | 40 sps | 10 Hz |

### Aliasing demonstration using pyqtgraph

ℹ️ Prerequisite: `pip install "pyqtgraph==0.12.4"`

```python3
## 7
## Try this. 
## The instructor will demonstrate...
## 1. How to show the FFT of the signal
## 2. The effects of resampling / decimating the signal

import pyqtgraph as pg
from pcdr import makeWave

## QT GUI Boilerplate setup
pg.mkQApp()
gview = pg.GraphicsView()
glayout = pg.GraphicsLayout()
gview.setCentralWidget(glayout)
gview.show()
## Create two plots, plot the same wave on each
p1 = glayout.addPlot()
p2 = glayout.addPlot()
x, y = makeWave(50, 10, "real", seconds=2)
curve1 = p1.plot(x, y, symbol="t")
curve2 = p2.plot(x, y, symbol="t")

if __name__ == '__main__':
    pg.exec()
```

### Aliasing demonstration using gqrx

Aliasing in signal processing happens when you measure a signal that is outside of what your sample rate allows.

1. Open GQRX on the instructor screen. Tune to the broadcast FM range.
2. Have a student run the noise jammer, tuned to near the top end of the spectrum.
3. Slowly raise the noise jammer past the right edge. It will incorrectly appear on the left edge due to aliasing.
 
### How to fix?

In the FM Radio flowgraph, we use the "hardware_filter" checkbox to do analog filtering inside the Hack RF.

In GQRX, you should be able to use the same filter, but as far as I can tell, there's a bug that prevents that from working, unfortunately. (Either that, or I'm doing it wrong.)
