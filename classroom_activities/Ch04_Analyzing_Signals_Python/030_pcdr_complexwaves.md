### Adding waves

When the signal is made up of a single wave, we can fairly easily identify the frequency of that wave. Even if there are two frequencies present, it's not too difficult to distinguish the frequencies that are present:

```python3
## 4
## Try this example, which plots a 2 Hz wave and a 25 Hz wave.
## Notice that we're only plotting the sum of the waves.
## Can you still distinguish the two separate frequencies?
import matplotlib.pyplot as plt
from pcdr import makeRealWave_time

seconds = 2
samp_rate = 500
timestamps, wave1 = makeRealWave_time(seconds=seconds, samp_rate=samp_rate, freq=2)
timestamps, wave2 = makeRealWave_time(seconds=seconds, samp_rate=samp_rate, freq=25)
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

