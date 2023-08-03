from pcdr.osmocom_queued_tx_flowgraph import send_data

import numpy as np


dat_pieces = [np.ones(256), np.zeros(256), np.ones(256), np.zeros(256)]
dat = []
for i in range(10000):
    dat.append(np.complex64(np.concatenate(dat_pieces)))
send_data(dat, center_freq=2.4e9)
