"""
Reads the specified file,
Adds random noise,
scales down (to avoid amplitude being unrealistically large)
writes result to a new file.
"""
import numpy as np

infilename = "unknown_signal_1.complex"
outfilename = "generated_noisy_signal.complex"
scale_factor = 0.2

dat = np.fromfile(infilename, dtype=np.complex64)

noise_real = np.random.normal(0, .5, len(dat))
noise_imag = np.random.normal(0, .5, len(dat))

noisydat = dat + noise_real + 1j*noise_imag
scaled = scale_factor * noisydat
propertype = np.complex64(scaled)

propertype.tofile(outfilename)
