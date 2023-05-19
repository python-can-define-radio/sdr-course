import numpy as np
import matplotlib.pyplot as plt

t_max = 2 * np.pi
times = np.linspace(0, t_max, 200)
volt1 = np.cos(times)
volt2 = np.sin(times)
plt.plot(times, volt1, "b.")
plt.plot(times, volt2, "r.")
plt.show()


# voltages = np.exp(times * 1j)

# plt.figure()
# plt.plot(times, voltages.real, "b.")
# plt.plot(times, voltages.imag, "r.")
# plt.figure()
# plt.show()