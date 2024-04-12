## OOK Transmitting using Python: Lesson 2

Now that we've seen some wave theory, let's prepare to transmit to the Hack RF.

```python3
## Unfinished exercise
import matplotlib.pyplot as plt
from pcdr.wavegen import make_timestamps_seconds, makeRealWave, makeComplexWave
from pcdr.modulators import ook_modulate
from pcdr.gnuradio_sender import gnuradio_send



timestamps = make_timestamps_seconds(seconds=1.0, num_samples=int(2e6))
wave = makeComplexWave_fixme_due_to_function_changes(timestamps, freq=4)
modded = ook_modulate([1, 0, 1, 0], bit_length=int(500e3))
fully_modded = modded * wave
gnuradio_send(fully_modded, center_freq=100e6, samp_rate=2e6)

## Actual transmission frequency: 100,000,004 Hz = 100.0000004 MHz
## TODO: decide what to do with imaginary part
plt.plot(timestamps, fully_modded.real, "*-", markersize=20)
plt.show()
```
