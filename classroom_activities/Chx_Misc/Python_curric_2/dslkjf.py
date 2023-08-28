from pcdr import gnuradio_simulate, makeComplexWave_time
import numpy as np

timestamps, wave = makeComplexWave_time(2, 2e6, 50e3)
# wave = np.complex64(np.linspace(0, 1, 101) + 1j * np.linspace(-0.1, 0.9, 101))

# (Pdb) p output_items[0][0][2]
# (1+0j)
# (Pdb) p output_items[0][0][3]
# (0.98768836+0.15643446j)

gnuradio_simulate(wave, 100e6, 2e6, prepend_zeros=2)