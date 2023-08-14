from __future__ import annotations
import deal
import numpy as np

from pcdr.osmocom_queued_rx_flowgraph import osmocom_source_to_queue
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.helpers import queue_to_list

# def gnuradio_receive(
#         center_freq: float,
#         samp_rate: float,
#         if_gain: int = 16,
#         input_from: str = "hackrf",
#         device_args: str = "hackrf=0"):
#     raise NotImplementedError()


class Gnuradio_receiver():

    def __init__(self, center_freq: float, samp_rate: float, if_gain: int = 32, bb_gain: int = 42, chunk_size: int = 1024, device_args: str = "hackrf=0"):
        tb = osmocom_source_to_queue(center_freq, samp_rate, chunk_size, device_args, if_gain, bb_gain)
        self.tb = tb
        self.__chunk_size = chunk_size
        configure_graceful_exit(tb)
    
    def start(self):
        self.tb.start()

    def stop(self):
        self.tb.stop()

    def wait(self):
        self.tb.wait()
    
    @deal.ensure(lambda _: len(_.result) == _.self.__chunk_size)
    def get(self):
        """Returns a chunk from the queue of accumulated received data."""
        return self.tb.get()
    
    def get_all(self) -> list[np.ndarray]:
        """Warning: this may or may not work while the flowgraph is running."""
        return self.tb.data_queue_sink.queue_get_all()

    