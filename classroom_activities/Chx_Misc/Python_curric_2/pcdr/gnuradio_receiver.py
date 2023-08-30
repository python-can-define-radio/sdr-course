from typing import List, Tuple
import deal
import numpy as np
import time

from pcdr.osmocom_queued_rx_flowgraph import osmocom_source_to_queue
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.helpers import queue_to_list


@deal.pre(lambda _: 1e6 <= _.center_freq <= 6e9)
@deal.pre(lambda _: 2e6 <= _.samp_rate <= 20e6)
@deal.pre(lambda _: _.if_gain in [0, 8, 16, 24, 32, 40])
@deal.pre(lambda _: _.bb_gain in range(0, 62+1, 2), message="bb_gain must be one of 0, 2, 4, 6, ... 58, 60, 62")
def gnuradio_receive(
        center_freq: float,
        samp_rate: float,
        seconds: float,
        if_gain: int = 32,
        bb_gain: int = 42,
        device_args: str = "hackrf=0",
        chunk_size: int = 1024) -> np.ndarray:
    """Receive for APPROXIMATELY `seconds` seconds."""
    tb = osmocom_source_to_queue(center_freq, samp_rate, chunk_size, device_args, if_gain, bb_gain)
    configure_graceful_exit(tb)
    tb.start()
    time.sleep(seconds)
    tb.stop()
    tb.wait()
    rx_data = np.array(tb.get_all())
    return rx_data.flatten()



class Gnuradio_receiver():

    def __init__(self, center_freq: float, samp_rate: float, if_gain: int = 32, bb_gain: int = 42, device_args: str = "hackrf=0", chunk_size: int = 1024):
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
    
    def get_all(self) -> List[np.ndarray]:
        """Warning: this may or may not work while the flowgraph is running."""
        return self.tb.data_queue_sink.queue_get_all()
