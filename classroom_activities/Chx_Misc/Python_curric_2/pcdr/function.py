from typing import Optional
from typeguard import typechecked
import numpy as np
from gnuradio import gr, blocks
from pcdr.our_GR_blocks import Blk_queue_source, Blk_queue_sink
from pcdr.helpers import getSize



class _QueuedBothEnds:
    """
    Sets up a top block that does
    queue - vecstream - proc - streamvec - queue.

    See notes on QueuedSource and QueuedSink regarding args.
    """
    @typechecked
    def __init__(self, 
                 ProcessBlk, 
                 in_dtype: type, 
                 out_dtype: type, 
                 in_chunk_size: int, 
                 out_chunk_size: int,
                 proc_blk_args: list = [],
                 timeout: Optional[float] = None):
        self.tb = gr.top_block()
        self.__source_q = Blk_queue_source(in_dtype, in_chunk_size, timeout=timeout)
        self.__vector_to_stream = blocks.vector_to_stream(getSize(in_dtype), in_chunk_size)
        self.__proc = ProcessBlk(*proc_blk_args)
        self.__stream_to_vec = blocks.stream_to_vector(getSize(out_dtype), out_chunk_size)
        self.__sink_q = Blk_queue_sink(out_dtype, out_chunk_size)
        self.tb.connect(self.__source_q, self.__vector_to_stream, 
                          self.__proc,
                          self.__stream_to_vec, self.__sink_q)
    
    def put(self, val: np.ndarray):
        return self.__source_q.queue.put(val)

    def get(self) -> np.ndarray:
        return self.__sink_q.queue.get()
    
    def proc(self, chunk: np.ndarray) -> np.ndarray:
        self.put(chunk)
        return self.get()




# @typechecked
# def _functionalize_proc_blk(ProcessBlk, 
#                  in_dtype: type, 
#                  out_dtype: type, 
#                  in_chunk_size: int, 
#                  out_chunk_size: int,
#                  proc_blk_args: list = []):
#     qbe = _QueuedBothEnds(ProcessBlk, in_dtype, out_dtype, in_chunk_size, out_chunk_size, proc_blk_args, timeout=1)
#     qbe.tb.start()
#     return run


## TODO
#     analog.wfm_rcv(
# 	quad_rate=,
# 	audio_decimation=,
# )
    














# from pcdr.wavegen import makeWave
# from gnuradio import blocks, filter
# from gnuradio.filter import firdes
# import numpy as np
# import matplotlib.pyplot as plt
 
# samp_rate = 2e6
 
# t, w1 = makeWave(samp_rate, 20_000, "complex", seconds=1/1_000)
# t, w2 = makeWave(samp_rate, 1_000, "complex", seconds=1/1_000)
# combined = w1 + w2
 
# band_pass_filter = filter.fir_filter_ccc(
#     1,
#     firdes.complex_band_pass(
#         1,
#         samp_rate,
#         -20e3,
#         20e3,
#         30e3))
 
 
# qbe = _QueuedBothEnds(band_pass_filter,
#                               np.complex64,
#                               np.complex64,
#                               in_chunk_size=len(combined),
#                               out_chunk_size=len(combined),
#                               )
 
# filtered = qbe.proc(combined)
# plt.plot(t, combined.real)
# plt.plot(t, combined.imag)
# plt.show()