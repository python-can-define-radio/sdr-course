import random
import time

import numpy as np

import pcdr._queue.sink as qsink
from pcdr._wavegen import random_normal, makeWave


if __name__ == "__main__":
    freqs = [104.3e6, 107.7e6]   # Hz
    start_freq = freqs[0]   # Hz
    samp_rate = 2e6  # samples per second
    delay = 0.2  # seconds
    chunk_size = int(samp_rate * delay)  # samples
    ones = np.ones(chunk_size)  # values to be transmitted
    osmosink = qsink.osmosdr_sink("hackrf", "0", samp_rate,
                                start_freq, if_gain=45, chunk_size=chunk_size)
    while True:
        osmosink.put(ones)   # enque a chunk of data to be transmitted
        osmosink.set_center_freq(random.choice(freqs))
        time.sleep(delay)


# sig = random_normal(chunk_size, np.complex64)
# 
