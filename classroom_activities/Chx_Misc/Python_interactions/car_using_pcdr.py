from pcdr.v0_compat import gnuradio_send, ook_modulate
import numpy as np

buncha_1_0 = [1,0] * 35
fourLong = [1,1,1,0] * 4

carsig_bits = fourLong + buncha_1_0
carsig = ook_modulate(carsig_bits, bit_length=1055)
gnuradio_send(carsig, center_freq=49.86e6, samp_rate=2e6, if_gain=35, repeat=True)
