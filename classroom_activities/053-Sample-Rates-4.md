## Sample Rate practice problems

Run this. You'll see that it plots a very rough sine wave.

```python3
import matplotlib.pyplot as plt

temps = [0.0, 2.3, 5, 10.3, 12.2, 12.5, 13.5, 15, 14, 4, 0, -9, -11, -12.5, -15, -16, -14.2, -12.5, -10, -5]

plt.plot(temps, "o")    #  the "o" means to use circles as markers of the points

plt.show()
```

Your tasks:

1. How many samples are there?
2. If your measurement tool was measuring with a sample rate of 10 samples per second, then how many seconds of data is this?
3. If the sample rate was instead 20 samples per second, then how many seconds of data is this?
4. If the sample rate was instead 40 sps (samples per second), then how many seconds of data is this?
5. How many full cycles of the rough sine wave appear to be depicted?
6. If the sample rate was 40 samples per second, then what is the frequency of the rough sine wave?
7. Fix the data so that the sine wave is clean.

<details><summary>Answers:</summary>
  
1. 20 samples
2. 2 seconds
3. 1 second
4. 0.5 seconds
5. 1 cycle
6. 2 cycles per second, or, equivalently, 2 Hz. If the sample rate = 40 sps, then the data given is half a second. Our given wave completes one full cycle in this time, and would therefore complete two cycles in a full second.
7. (The answer is graphical. If you're in class, ask an instructor or another student.)  
  
</details>
