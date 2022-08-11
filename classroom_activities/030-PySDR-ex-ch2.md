
#1. Try this. What is the frequency of the wave?

```python
import numpy as np
import matplotlib.pyplot as plt

times = np.linspace(0, 2, 500)
sig = np.sin(3 * 2 * np.pi * times)

plt.plot(times, sig, '.')
plt.show()
```

#2. Try this. What is the frequency of the wave?

```python
times = np.linspace(0, 2, 500)
sig = np.sin(4 * 2 * np.pi * times)

plt.plot(times, sig, '.')
plt.show()
```

#3. Copy and modify the previous example so that the wave is 1 Hz. Verify that it worked.

#4. Copy and modify the previous example so that the wave is 5 Hz. Verify that it worked.

#4b. Copy and modify the previous example so that the amount of time is 3 seconds. Verify that it worked.

#4c. Copy and modify the previous example so that the amount of time is 1 second. Verify that it worked.

#4d. Copy and modify the previous example so that the amplitude is 3. Hint: this will require multiplying.

#5. Try this.

```python
## This is NOT a "carrier wave" situation;
## it's simply two waves added.
times = np.linspace(0, 1, 5000)
first_sig = np.sin(2 * 2 * np.pi * times)
second_sig = np.sin(20 * 2 * np.pi * times)
combined = first_sig + second_sig

plt.plot(times, combined, '.')
plt.show()
```

#6. Try this.
```python3
## This is amplitude modulation.
## The 20 Hz wave is the carrier.
times = np.linspace(0, 1, 5000)
first_sig = np.sin(2 * 2 * np.pi * times)
second_sig = np.sin(20 * 2 * np.pi * times)
combined = (first_sig + 2) * second_sig

plt.plot(times, combined, '.')
plt.show()
```

#7. Try this.

```python3
times = np.linspace(0, 1, 100)
sig = np.sin(3 * 2 * np.pi * times)
freqs = np.fft.fftshift(np.fft.fft(sig))
posOnly = freqs[50:]
f = np.linspace(0, 50, 50)

plt.plot(times, sig, '.')
plt.show()
plt.plot(f, abs(posOnly), '.')
plt.show()
```


#8. Try this.
```python3
numMeas = 100 
maxTime = 1    # seconds

## By definition, sample rate is measurements per time
samp_rate = numMeas / maxTime

## Nyquist says we can't measure anything higher than 
## half the sample rate
maxMeasFreq = samp_rate // 2

print("Sample rate:", samp_rate)
print("Highest measurable freq:", maxMeasFreq)

times = np.linspace(0, maxTime, numMeas)

sig = np.sin(3 * 2 * np.pi * times)

freqs = np.fft.fftshift(np.fft.fft(sig))

## For now, we're only looking at positive frequencies.
halfway = len(freqs) // 2
posFreqsOnly = freqs[halfway:]
f = np.linspace(0, maxMeasFreq, halfway)

plt.subplot(2, 1, 1)
plt.plot(times, sig, '.')

plt.subplot(2, 1, 2)
plt.plot(f, abs(posFreqsOnly), '.')
plt.show()
```

#9. Copy and modify the previous example so that it has two signals added.
