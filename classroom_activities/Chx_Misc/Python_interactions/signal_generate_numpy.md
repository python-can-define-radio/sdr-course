## Task

Make some fake data that looks like this in time:


- First 8192 samples: Zeros
- Next 8192 samples: One pure sine wave on 3 Hz (freq of inters)
- Next 8192 samples: Zeros
- Next 8192 samples: One pure sine wave on the wrong freq
- Next  8192 samples: A noisy sine wave (add a pure wave to some random noise)
- Next  8192 samples: Just noise

You'll prob want the np.concatenate

THEN
Using a for loop (or your mechnaism of cohice)
- Take groups of 4096 smaples.  Each group will pertain to a unique time period.
- Do an FFT on each group of samples
- Check whether there is activity surpassing a certain (arbitrary) threshold on an arbitrary frequency (ex: 3 Hz) within each group.





### Example code that relates:

```python3
import numpy as np
import matplotlib.pyplot as plt


if False:
    timePoints = np.linspace(0, 1, 20, endpoint=False)

    plus2 = timePoints + 2
    timeshundred = timePoints * 100
    wavey = np.sin(10 * timePoints)

    plt.subplot(3, 1, 1)
    plt.plot(plus2)
    plt.subplot(3, 1, 2)
    plt.plot(timeshundred)
    plt.subplot(3, 1, 3)
    plt.plot(wavey)
    plt.show()


##########################
## Example 2
##########################

numSamples = 100
tMax = 1  # second(s)
samp_rate = numSamples / tMax  # Hz
timePoints = np.linspace(0, tMax, numSamples, endpoint=False)

wave = np.sin(3 * 2 * np.pi *  timePoints)
# complexwave = np.exp(3 * 2j * np.pi *  timePoints)
## Equivalently:
complexwave = np.cos(3 * 2 * np.pi *  timePoints) + 1j*np.sin(3 * 2 * np.pi *  timePoints)

fftOfReal = abs(np.fft.fftshift(np.fft.fft(wave)))
fftOfComplex = abs(np.fft.fftshift(np.fft.fft(complexwave)))

fft_freqs = np.linspace(-samp_rate/2, samp_rate/2, numSamples, endpoint=False)

plt.subplot(2, 2, 1)
plt.plot(timePoints, wave, "g")
plt.subplot(2, 2, 2)
plt.plot(fft_freqs, fftOfReal, "g")

plt.subplot(2, 2, 3)
plt.plot(timePoints, complexwave.real, "blue")
plt.plot(timePoints, complexwave.imag, "red")
plt.subplot(2, 2, 4)
plt.plot(fft_freqs, fftOfComplex, "blue")
plt.show()




# fakedata = np.sin()
# absval = abs(samples)
```



