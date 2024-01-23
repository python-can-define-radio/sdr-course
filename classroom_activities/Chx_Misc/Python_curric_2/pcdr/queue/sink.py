"""
Queue-wrapped GNU Radio sink blocks.

Example usage:
TODO: fix
# >>> import pcdr.queue.sink
# >>> from pathlib import Path
# >>> p = Path("temp_dir_for_tests") / "somecomplexfile.complex"
# >>> filesink = pcdr.queue.sink.file_sink(np.complex64, str(p), samp_rate=1280, timeout=1.0)
# >>> filesink.start()
# >>> filesink.wait()
Queue is empty, block will now report 'done' to GNU Radio flowgraph
# >>> p.unlink()
"""
from typeguard import typechecked
from gnuradio import gr, blocks
from termcolor import cprint
from pcdr.helpers import getSize
from pcdr.our_GR_blocks import Blk_queue_source
from pcdr.queue import ChunkSizeNonIntegerError
import numpy as np
from typing import Optional
import osmosdr
import time


@typechecked
def _post_warn_chunk_size(chunk_size: int):
    """
    These will have output:
    >>> _post_warn_chunk_size(5)
    Your chunk size 5 is not a power of 2...
    >>> _post_warn_chunk_size(6)
    Your chunk size 6 is not a power of 2...
    >>> _post_warn_chunk_size(527)
    Your chunk size 527 is not a power of 2...
    
    This one will have no output:
    >>> _post_warn_chunk_size(8)
    """
    cs = chunk_size
    ## If chunk size is not a power of 2
    if cs & (cs-1) != 0:
        cprint(f"Your chunk size {cs} is not a power of 2, so GNU Radio likely issued 'buffer_double_mapped' warning(s). This warning can be ignored, as it is only performance-related, not functionality-related.\n", "green")


@typechecked
def _compute_chunk_size(samp_rate: float, chunk_size: Optional[int]) -> int:
    """
    >>> _compute_chunk_size(350, None)
    35
    >>> _compute_chunk_size(321, None)
    Traceback (most recent call last):
      ...
    pcdr.queue.ChunkSizeNonIntegerError: Chunk size must be specified if samp rate is not divisible by 10.

    If chunk size is specified, simply return it:
    >>> _compute_chunk_size(321, 300)
    300
    """
    if chunk_size != None:
        return chunk_size
    divby = 10
    if samp_rate % divby != 0:
        raise ChunkSizeNonIntegerError(f"Chunk size must be specified if samp rate is not divisible by {divby}.")
    return int(samp_rate // divby)


class _QueuedSink:
    """
    Sets up a top block that...
     - Provides access to a queue via `.put()`
     - Feeds the queued data into the given sink block

    The `dtype` arg should be the output type of `SinkBlk`.
    The `chunk_size` arg is how many items are produced per chunk. Larger values are usually more efficient, but too large will delay access to data and possibly reach the RAM max.
    """
    @typechecked
    def __init__(self,
                 sinkBlk,
                 dtype: type,
                 chunk_size: int,
                 autostart: bool,
                 timeout: Optional[float] = None):
        self.tb = gr.top_block()
        self.__source_q = Blk_queue_source(dtype, chunk_size, timeout)
        self.__vector_to_stream = blocks.vector_to_stream(getSize(dtype), chunk_size)
        self._sink = sinkBlk
        self.tb.connect(self.__source_q, self.__vector_to_stream, self._sink)
        _post_warn_chunk_size(chunk_size)
        if autostart:
            self.start()
    
    def start(self):
        self.tb.start()
        
    def put(self, data: np.ndarray):
        """Enqueues a chunk of data to be fed to the sink."""
        return self.__source_q.queue.put(data)

    def stop(self):
        self.tb.stop()
    
    def wait(self):
        self.tb.wait()
    
    def mark_done(self):
        self.__source_q.marked_done = True
        

class file_sink(_QueuedSink):
    @typechecked
    def __init__(self,
                 dtype: type,
                 filename: str,
                 append: bool = False,
                 unbuffered: bool = False,
                 *, samp_rate: float,
                 chunk_size: Optional[int] = None,
                 timeout: Optional[float] = None):
        chunk_size = _compute_chunk_size(samp_rate, chunk_size)
        assert "NEED TO UPDATE THE INIT. NEED TO DECIDE ABOUT AUTOSTART." == False
        super().__init__(
            blocks.file_sink(getSize(dtype), filename, append),
            dtype,
            chunk_size,
            timeout)
        self._sink.set_unbuffered(unbuffered)


class wavfile_sink(_QueuedSink):
    @typechecked
    def __init__(self,
                 filename: str,
                 n_channels: int = 1,
                 sample_rate: int = 48000,
                 format = "blocks.FORMAT_WAV",   # TODO fix
                 subformat = "blocks.FORMAT_PCM_16",  # TODO fix
                 append: bool = False,
                 *, chunk_size: int):
        chunk_size = _compute_chunk_size(sample_rate, chunk_size)
        super().__init__(
            blocks.wavfile_sink(filename, n_channels, sample_rate, format, subformat, append),
            np.float32,
            chunk_size)


class osmosdr_sink(_QueuedSink):
    @typechecked
    def __init__(self,
                 device_name: str,
                 device_id: str,
                 samp_rate: float,
                 center_freq: float,
                 if_gain: int,
                 *, chunk_size: Optional[int] = None,
                 autostart: bool = True,
                 ):
        """
        `device_name`: One of the supported osmocom devices, such as hackrf, bladerf, etc (see the osmocom docs)
        `device_id`: A zero-based index ("0", "1", etc), or the partial serial number of the device, which can be gotten from GQRX

        >>> 
        """
        chunk_size = _compute_chunk_size(samp_rate, chunk_size)
        device_args = f"{device_name}={device_id}"
        self.gr_sink = osmosdr.sink(device_args)
        super().__init__(
            self.gr_sink, np.complex64, chunk_size, autostart
        )
        self.gr_sink.set_time_now(  
            # This corresponds to the "PC Clock" option in GRC,
            # which is known to work with our hardware.
            # Long term TODO: consider providing an __init__ arg as GRC does
            osmosdr.time_spec_t(time.time()),
            osmosdr.ALL_MBOARDS)
        self.gr_sink.set_sample_rate(samp_rate)
        self.set_center_freq(center_freq)
        self.gr_sink.set_if_gain(if_gain)
    
    def set_center_freq(self, samp_rate: float) -> float:
        return self.gr_sink.set_center_freq(samp_rate)
