
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
times = np.linspace(0, 2, 5000)
first_sig = np.sin(2 * 2 * np.pi * times)
second_sig = np.sin(20 * 2 * np.pi * times)
combined = first_sig + second_sig

plt.plot(times, combined, '.')
plt.show()
```
