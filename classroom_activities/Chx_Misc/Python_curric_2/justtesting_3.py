## "Easy" lesson
# from pcdr import gnuradio_send, ook_modulate

# modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))
# gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)

# ## "Level 2" lesson

from pcdr import ook_modulate
import pcdr._queue.sink as qsink

if __name__ == "__main__":
    samp_rate = 2e6
    center_freq = 434e6
    if_gain = 42
    modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))
    osmosink = qsink.osmosdr_sink("hackrf", "0", samp_rate, center_freq,
                                if_gain, chunk_size=len(modulated))
    for x in range(100):
        osmosink.put(modulated)
        print(x)
    osmosink.mark_done()
    osmosink.wait()
