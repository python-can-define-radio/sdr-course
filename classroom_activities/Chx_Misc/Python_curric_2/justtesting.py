import numpy as np
import time
import matplotlib.pyplot as plt
from pcdr import Gnuradio_receiver


if __name__ == "__main__":
    samp_rate = 2e6
    receiver = Gnuradio_receiver(center_freq=104.3e6, samp_rate=samp_rate, chunk_size=1024)
    receiver.start()
    time.sleep(2)
    receiver.stop()
    receiver.wait()

    # data = receiver.get()
    # plt.plot(abs(np.fft.fftshift(np.fft.fft(data))))
    # plt.show()

    flattened = np.array(receiver.get_all()).flatten()

    print(f"Approx number of seconds of data: {len(flattened) / samp_rate}")
    plt.specgram(flattened, NFFT=4096, Fs=samp_rate)
    plt.show()
