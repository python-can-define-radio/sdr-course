from pcdr import makeComplexWave_time
import matplotlib.pyplot as plt

timestamps, wave = makeComplexWave_time(10, 2e6, 50e3)
plt.plot(wave[-10_000:].real, color="blue")
plt.plot(wave[-10_000:].imag, color="red")
plt.show()
