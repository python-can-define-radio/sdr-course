from typing import List, Tuple
import numpy as np
import time
from gnuradio import gr

from pcdr.osmocom_queued_rx_flowgraph import osmocom_source_to_queue_sink, file_source_to_queue_sink
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.helpers import queue_to_list, validate_hack_rf_receive
from pcdr.types_and_contracts import SupportsQueueSink




def __run_block_and_return_queue_contents(tb: SupportsQueueSink, seconds: float):
    """Note: if seconds=-1, that means 'read till done'.
    Don't use seconds=-1 for the osmocom, as it will never finish."""
    ## this assertion should be done as a type annotation, but I haven't yet figured out
    ## how to do that with multiple types.
    assert isinstance(tb, gr.top_block)
    configure_graceful_exit(tb)
    tb.start()
    if seconds == -1:
        tb.wait()
    else:
        time.sleep(seconds)
        tb.stop()
        tb.wait()
    rx_data = np.array(tb.queue_sink.get_all())
    assert isinstance(rx_data, np.ndarray)
    return rx_data.flatten()



def gnuradio_receive(
        center_freq: float,
        samp_rate: float,
        seconds: float,
        if_gain: int = 32,
        bb_gain: int = 42,
        device_args: str = "hackrf=0",
        chunk_size: int = 1024) -> np.ndarray:
    """Receive for APPROXIMATELY `seconds` seconds."""
    ## TODO: This should be device_name instead of device_args.
    validate_hack_rf_receive(device_args, samp_rate, center_freq, if_gain, bb_gain)
    tb = osmocom_source_to_queue_sink(center_freq, samp_rate, if_gain, bb_gain, device_args, chunk_size)
    return __run_block_and_return_queue_contents(tb, seconds)



def gnuradio_read_file(filename: str, chunk_size: int = 1024, repeat: bool = False) -> np.ndarray:
    """Read from a complex-formatted file.
    The type should be np.complex64.
    Confusingly, GNU Radio Companion refers to this as 'Complex 32'.
    
    For general-purpose file reading, `np.fromfile` is superior.
    This function is primarily intended to mimic `gnuradio_receive`
    to test the non-SDR-peripheral aspects of that implementation.
    """
    tb = file_source_to_queue_sink(filename, chunk_size, repeat)
    return __run_block_and_return_queue_contents(tb, -1)



class Gnuradio_receiver():

    def __init__(self, center_freq: float, samp_rate: float, if_gain: int = 32, bb_gain: int = 42, device_args: str = "hackrf=0", chunk_size: int = 1024):
        tb = osmocom_source_to_queue_sink(center_freq, samp_rate, chunk_size, device_args, if_gain, bb_gain)
        self.tb = tb
        self.__chunk_size = chunk_size
        configure_graceful_exit(tb)
    
    def start(self):
        self.tb.start()

    def stop(self):
        self.tb.stop()

    def wait(self):
        self.tb.wait()
    
    def get(self) -> np.ndarray:
        """Returns a chunk from the queue of accumulated received data."""
        result = self.tb.queue_sink.get()
        assert len(result == self.__chunk_size)
        return result
    
    def get_all(self) -> List[np.ndarray]:
        """Warning: this may or may not work while the flowgraph is running."""
        return self.tb.queue_sink.get_all()
