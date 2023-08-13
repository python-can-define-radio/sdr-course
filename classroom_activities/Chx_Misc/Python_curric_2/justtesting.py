from queue import SimpleQueue
import numpy as np
from pcdr import pad_chunk_queue, ook_modulate, createTimestamps, makeRealWave


samp_rate = 50
modded = ook_modulate(data=[1, 0, 1, 0, 1, 0, 1, 1], bit_length=25)
t = len(modded) / samp_rate
timestamps = createTimestamps(seconds=t, num_samples=len(modded))
wave = makeRealWave(timestamps, freq=4)
fully_modded = modded * wave
noisy = TODO
random_amount_of_no_signal_at_beginning = TODO

fakeQueue = pad_chunk_queue(TODO, arbitrary_size)

print("TODO: demodulate the signal")

