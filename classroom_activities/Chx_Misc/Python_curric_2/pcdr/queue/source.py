from typeguard import typechecked
from gnuradio import gr, blocks
from pcdr.helpers import getSize
from pcdr.our_GR_blocks import Blk_queue_sink
import numpy as np



class QueuedSource:
    """
    Sets up a top block that...
     - Runs the source block
     - Puts the output of said block into a queue
     - Provides access to the queue via `.get()`

    The `dtype` arg should be the output type of `SourceBlk`.
    The `chunk_size` arg is how many items are produced per chunk. Larger values are usually more efficient, but too large will delay access to data and possibly reach the RAM max.
    """
    @typechecked
    def __init__(self, SourceBlk, dtype: type, chunk_size: int, source_block_args: list = []):
        self.__tb = gr.top_block()
        self.__source = SourceBlk(*source_block_args)
        self.__stream_to_vec = blocks.stream_to_vector(getSize(dtype), chunk_size)
        self.__sink_q = Blk_queue_sink(dtype, chunk_size)
        self.__tb.connect(self.__source, self.__stream_to_vec, self.__sink_q)
        self.__tb.start()
    
    def get(self) -> np.ndarray:
        return self.__sink_q.queue.get()
