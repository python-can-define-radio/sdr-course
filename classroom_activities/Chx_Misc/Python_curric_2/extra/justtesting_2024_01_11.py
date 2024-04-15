import pcdr._queue.sink as qsink
from pcdr._wavegen import random_normal, makeWave


if __name__ == "__main__":
    samp_rate = 2e6  # units: samples per second
    hop_delay = 0.25  # units: seconds
    chunk_size = int(samp_rate * hop_delay)
    freqs = [104.3e6, 107.7e6]
    osmosink = qsink.osmosdr_sink("hackrf", "0", samp_rate, freqs[0],
                                if_gain=45, chunk_size=chunk_size)
    timestamps, sig = makeWave(samp_rate, 10e3, "complex", num=chunk_size)
    while True:
        osmosink.put(sig)
        # time.sleep(hop_delay)
        # osmosink.gr_sink.set_center_freq(107.7e6)
        # osmosink.set_center_freq(random.choice(freqs))
    osmosink.mark_done()
    osmosink.wait()


# sig = random_normal(chunk_size, np.complex64)
# 
