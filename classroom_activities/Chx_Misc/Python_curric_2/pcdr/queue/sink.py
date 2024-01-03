from typeguard import typechecked
from gnuradio import gr, blocks
from termcolor import cprint
from pcdr.helpers import getSize
from pcdr.our_GR_blocks import Blk_queue_source
import numpy as np
from typing import Optional



def _post_warn_chunk_size(chunk_size: int):
    """
    These will have output:
    >>> _post_warn_chunk_size(5)
    Your chunk size 5 is not a power of 2...
    >>> _post_warn_chunk_size(6)
    Your chunk size 6 is not a power of 2...
    >>> _post_warn_chunk_size(527)
    This is intentionally a wrong test to remind us to verify this works. Your chunk size 527 is not a power of 2...
    
    This one will have no output:
    >>> _post_warn_chunk_size(8)
    """
    cs = chunk_size
    ## If chunk size is not a power of 2
    if cs & (cs-1) != 0:
        cprint(f"Your chunk size {cs} is not a power of 2, so GNU Radio likely issued 'buffer_double_mapped' warning(s). This warning can be ignored, as it is only performance-related, not functionality-related.\n", "green")


class ChunkSizeNonIntegerError(Exception):
    pass


def _compute_chunk_size(samp_rate: float, chunk_size: Optional[int]) -> int:
    """
    >>> _compute_chunk_size(350, None)
    35
    >>> _compute_chunk_size(321, None)
    Traceback...

    If chunk size is specified, simply return it:
    >>> _compute_chunk_size(321, 300)
    300
    """
    if chunk_size != None:
        return chunk_size
    divby = 10
    if samp_rate % divby != 0:
        raise ChunkSizeNonIntegerError(f"Chunk size must be specified if samp rate is not divisible by {divby}.")
    return samp_rate // 10


class _QueuedSink:
    """
    Sets up a top block that...
     - Provides access to a queue via `.put()`
     - Feeds the queued data into the given sink block

    The `dtype` arg should be the output type of `SinkBlk`.
    The `chunk_size` arg is how many items are produced per chunk. Larger values are usually more efficient, but too large will delay access to data and possibly reach the RAM max.
    """
    @typechecked
    def __init__(self, sinkBlk, dtype: type, chunk_size: int):
        self.__tb = gr.top_block()
        self.__source_q = Blk_queue_source(dtype, chunk_size)
        self.__vector_to_stream = blocks.vector_to_stream(getSize(dtype), chunk_size)
        self._sink = sinkBlk
        self.__tb.connect(self.__source_q, self.__vector_to_stream, self._sink)
        self.__tb.start()
        _post_warn_chunk_size(chunk_size)
    
    def put(self, val: np.ndarray):
        return self.__source_q.queue.put(val)

    def stop_and_wait(self):
        self.__tb.stop()
        self.__tb.wait()
        

class file_sink(_QueuedSink):
    def __init__(self, dtype: type, filename: str, append: bool = False, unbuffered: bool = False, *, samp_rate: float, chunk_size: Optional[int] = None):
        chunk_size = _compute_chunk_size(samp_rate, chunk_size)
        super().__init__(blocks.file_sink(getSize(dtype), filename, append), dtype, chunk_size)
        self._sink.set_unbuffered(unbuffered)


class wavfile_sink(_QueuedSink):
    @typechecked
    def __init__(self,
                 filename: str,
                 n_channels: int = 1,
                 sample_rate: int = 48000,
                 format: blocks.blocks_python.wavfile_format_t = blocks.FORMAT_WAV,
                 subformat: blocks.blocks_python.wavfile_subformat_t = blocks.FORMAT_PCM_16,
                 append: bool = False,
                 *, chunk_size: int):
        chunk_size = _compute_chunk_size(sample_rate, chunk_size)
        super().__init__(
            blocks.wavfile_sink(filename, n_channels, sample_rate, format, subformat, append),
            np.float32,
            chunk_size)

