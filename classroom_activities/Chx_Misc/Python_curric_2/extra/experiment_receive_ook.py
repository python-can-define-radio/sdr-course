# - GNU Radio tb: Get average signal strength on frequency band over a given amount of time
# osmocom source --> fft --> slice the array to get the desired frequency band; average that slice --> return as a single item.

# This allows easy queue fetching because you can fetch just one item, which is far easier to code!

# Something like this:
# data_under_inspection = []
# while True:
#     if does_start_with_preamble(dui):
#         demod_ook(dui)
#     dui.append(queue.get())
#     dui.removefirst()

# This is terribly inefficient because it involves checking the same data over-and-over, and I think that either removefirst or append are O(n), but WHO CARES because we're working at low data rates! I'm excited.

# def does start with preamble:
#   Preamble = [1, 1, 1, 1, 0...]
#   Check if 80% match

from pcdr import make_fft
import numpy as np
import matplotlib.pyplot as plt
from math import ceil

if __name__ == "__main__":
    # print(np.array_split([1,2,3,4,5,6,7,8,9], 9 / 2))
    dat = np.fromfile("ook_mini_content.iqdata", dtype=np.complex64)
    chunks = np.array_split(dat, ceil(len(dat)/4096))
    # print(len(chunks))
    for i, chunk in enumerate(chunks):
        sample_freqs, fft_mag = make_fft(chunk, samp_rate=20000)
        plt.plot(sample_freqs, fft_mag + i*10)
    plt.show()

