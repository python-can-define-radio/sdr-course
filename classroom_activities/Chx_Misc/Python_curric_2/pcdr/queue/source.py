from typing import Optional
from typeguard import typechecked
from gnuradio import gr, blocks
from pcdr.helpers import getSize
from pcdr.our_GR_blocks import Blk_queue_sink
import numpy as np



class _QueuedSource:
    """
    Sets up a top block that...
     - Runs the source block
     - Puts the output of said block into a queue
     - Provides access to the queue via `.get()`

    The `dtype` arg should be the output type of `SourceBlk`.
    The `chunk_size` arg is how many items are produced per chunk. Larger values are usually more efficient, but too large will delay access to data and possibly reach the RAM max.
    """
    @typechecked
    def __init__(self,
                 sourceBlk,
                 dtype: type,
                 chunk_size: int,
                 timeout: Optional[float] = None):
        self.tb = gr.top_block()
        self.__source = sourceBlk
        self.__stream_to_vec = blocks.stream_to_vector(getSize(dtype), chunk_size)
        self.__sink_q = Blk_queue_sink(dtype, chunk_size)
        self.tb.connect(self.__source, self.__stream_to_vec, self.__sink_q)
    
    def get(self) -> np.ndarray:
        return self.__sink_q.queue.get()
