## https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Custom_python_blocks/030-Basics-of-Python-blocks.md

import numpy as np
from gnuradio import gr, blocks, audio
import time
from queue import SimpleQueue
from numba import njit
import matplotlib.pyplot as plt
from typeguard import typechecked
from typing import Type




class Blk_sink_print(gr.sync_block):
    def __init__(self, only_print_1_in: int = 1):
        gr.sync_block.__init__(self, name='Print sink', in_sig=[np.float32], out_sig=[])
        self.only_print_1_in = only_print_1_in
        self.count = 0

    def work(self, input_items, output_items):
        if self.count == self.only_print_1_in:
            self.count = 0
            print(input_items[0][0])
            time.sleep(1e-6)
        self.count += 1
        return 1


class Blk_queue_sink(gr.sync_block):
    @typechecked
    def __init__(self, dtype: type, chunk_size: int):
        gr.sync_block.__init__(
            self,
            name='Python Block: Queue Sink',
            in_sig=[(dtype, chunk_size)],
            out_sig=[]
        )
        self.queue = SimpleQueue()

    def work(self, input_items, output_items):  
        datacopy = input_items[0][0].copy()
        self.queue.put(datacopy)
        return 1


@typechecked
def getSize(dtype: type) -> int:
    if dtype == np.complex64:
        return gr.sizeof_gr_complex
    elif dtype == np.float32:
        return gr.sizeof_float
    elif dtype == np.int32:
        return gr.sizeof_int
    elif dtype == np.int16:
        return gr.sizeof_short
    elif dtype == np.uint8:
        return gr.sizeof_char
    else:
        return NotImplementedError("Feel free to add more dtype matches")


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


class Blk_source_output_arb_num(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Source: the number 213', in_sig=[], out_sig=[np.float32])
        self.i = 0

    def work(self, input_items, output_items):
        output_items[0][0] = self.i
        output_items[0][1] = self.i + 1
        output_items[0][2] = self.i + 2
        self.i += 3
        return 3


class Blk_queue_source(gr.sync_block):
    @typechecked
    def __init__(self, dtype: type, chunk_size: int):
        gr.sync_block.__init__(self,
            name='Python Block: Queue Source',
            in_sig=[],
            out_sig=[(dtype, chunk_size)]
        )
        self.queue = SimpleQueue()

    def work(self, input_items, output_items):  
        output_items[0][0][:] = self.queue.get()
        return 1


class QueuedSink:
    """
    Sets up a top block that...
     - Provides access to a queue via `.put()`
     - Feeds the queued data into the given sink block

    The `dtype` arg should be the output type of `SinkBlk`.
    The `chunk_size` arg is how many items are produced per chunk. Larger values are usually more efficient, but too large will delay access to data and possibly reach the RAM max.
    """
    @typechecked
    def __init__(self, SinkBlk, dtype: type, chunk_size: int, sink_block_args: list = []):
        self.__tb = gr.top_block()
        self.__source_q = Blk_queue_source(dtype, chunk_size)
        self.__vector_to_stream = blocks.vector_to_stream(getSize(dtype), chunk_size)
        self.__sink = SinkBlk(*sink_block_args)
        self.__tb.connect(self.__source_q, self.__vector_to_stream, self.__sink)
        self.__tb.start()
    
    def put(self, val: np.ndarray):
        return self.__source_q.queue.put(val)


class LargerThanBufferError(Exception):
    pass


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



if __name__ == "__main__":
    # siz = 65536
    # samp_rate = 48000
    # qsour = QueuedSource(Blk_source_output_arb_num, np.float32, siz)
    # qsink = QueuedSink(blocks.wavfile_sink, np.float32, siz, ["testf.wav", 1, samp_rate, blocks.FORMAT_WAV, blocks.FORMAT_PCM_16])
    # qsink = QueuedSink(audio.sink, np.float32, siz, [samp_rate])

    # while True:
    # x = qsour.get()
    # seconds = x / samp_rate
    # y = np.sin(1000 * 2 * np.pi * seconds)
    # qsink.put(y)
    # y = np.sin(500 * 2 * np.pi * seconds)
    # qsink.put(y)
    # plt.plot(seconds[:200], y[:200], ".")
    # plt.show()


    # n = 8192
    # np.linspace(0, n, n, endpoint=False)

    chunk_size = 133
    sour = QueuedSource(Blk_source_output_arb_num, np.float32, chunk_size)
    sink = QueuedSink(Blk_sink_print, np.float32, chunk_size, sink_block_args=[100])
    while True:
        piece = sour.get()
        sink.put(piece)
    # time.sleep(5)
    # sour.stop_and_wait()
    # sink.stop_and_wait()



    ##################
    ## Ex 2 

    # import pcdr.sources
    # import pcdr.demod
    # import pcdr.sinks

    # hackrf = pcdr.sources.HackRF()
    # demodulator = pcdr.demod.WBFM()
    # audioSink = pcdr.sinks.audio()

    # freq = 104.3e6
    # while True:
    #     data = hackrf.get()
    #     audio = demodulator.process(data)
    #     audioSink.play(audio)
    #     time.sleep(2)
    #     hackrf.set_freq()
    #     freq += 0.2e6
        



