from queue import SimpleQueue
import numpy as np
import time
import matplotlib.pyplot as plt
from pcdr import Gnuradio_receiver



receiver = Gnuradio_receiver(center_freq=98e6, samp_rate=20e6, chunk_size=2**20)
receiver.start()
time.sleep(240)
receiver.stop()
receiver.wait()
listy = receiver.tb.data_queue_sink.queue_get_all()
print(len(listy) * len(listy[0]) / 20e6)
# import ipdb; ipdb.set_trace()
# receiver.stop()
# data = receiver.get()
# abs(np.fft.fftshift(np.fft.fft(data)))




