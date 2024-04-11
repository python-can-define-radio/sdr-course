"""For the record"""
from typeguard import typechecked
from queue import SimpleQueue
from gnuradio import gr
import numpy as np


class LargerThanBufferError(Exception):
    pass


class Blk_queue_sink_nonvec(gr.sync_block):
    @typechecked
    def __init__(self, dtype: type):
        gr.sync_block.__init__(
            self,
            name='Python Block: Queue Sink',
            in_sig=[dtype],
            out_sig=[]
        )
        self.queue = SimpleQueue()

    def work(self, input_items, output_items):  
        inp = input_items[0]
        ###  inp = 0 10 20 30 40 50 60 70 80 90
        ###  chunk_size = 
        fits_in_buffer = inp[:8192]
        self.queue.put(fits_in_buffer)
        return len(fits_in_buffer)


class QueuedSource_nonvec:
    @typechecked
    def __init__(self, SourceBlk, dtype: type, source_block_args: list = []):
        self.__tb = gr.top_block()
        self.__source = SourceBlk(*source_block_args)
        self.__sink_q = Blk_queue_sink_nonvec(dtype)
        self.__tb.connect(self.__source, self.__sink_q)
        self.__tb.start()
    
    def get(self) -> np.ndarray:
        return self.__sink_q.queue.get()

    def stop_and_wait(self):
        self.__tb.stop()
        self.__tb.wait()



class Blk_queue_source_nonvec(gr.sync_block):
    @typechecked
    def __init__(self, dtype: type):
        gr.sync_block.__init__(self,
            name='Python Block: Queue Source',
            in_sig=[],
            out_sig=[dtype]
        )
        self.queue = SimpleQueue()

    def work(self, input_items, output_items):  
        out = output_items[0]
        item = self.queue.get()
        n = len(item)
        if n > len(out):
            raise LargerThanBufferError(f"The length of the data was {n}, but the buffer limit is {len(out)}.")
        out[:n] = item
        return n


class QueuedSink_nonvec:
    @typechecked
    def __init__(self, SinkBlk, dtype: type, sink_block_args: list = []):
        self.__tb = gr.top_block()
        self.__source_q = Blk_queue_source_nonvec(dtype)
        self.__sink = SinkBlk(*sink_block_args)
        self.__tb.connect(self.__source_q, self.__sink)
        self.__tb.start()
    
    def put(self, val: np.ndarray):
        return self.__source_q.queue.put(val)

    def stop_and_wait(self):
        self.__tb.stop()
        self.__tb.wait()
