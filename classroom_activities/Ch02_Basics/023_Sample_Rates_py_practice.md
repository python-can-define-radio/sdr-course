<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Oct 06: 053-Sample-Rates-4.md
2023 Jan 04: 053-Sample-Rates-4-py-practice.md
2023 May 22: 023_Sample_Rates_py_practice.md
</pre>
</details>

## Sample Rate practice problems

Run this. Name it `rough_sine_wave.py`. You'll see that it plots a very rough sine wave.

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
7. There's more than one possible answer. If you're in class, ask an instructor or another student.  
   One of many valid answers would be this:  
   `[0.0, 4.64, 8.82, 12.14, 14.27, 15.0, 14.27, 12.14, 8.82, 4.64, 0.0, -4.64, -8.82, -12.14, -14.27, -15.0, -14.27, -12.14, -8.82, -4.64]`  
   &nbsp;  
   For those who are curious, that list was generated using this code:
   ```python3
   import numpy as np
  
   dat = 15*np.sin(np.linspace(0, 2 * np.pi, 20, endpoint=False))

   def roundtwo(x):
       return round(x, 2)
    
   datRounded = list(map(roundtwo, dat))
   print(datRounded)
   ```
  
</details>
