## https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Custom_python_blocks/030-Basics-of-Python-blocks.md

import numpy as np
from gnuradio import gr, blocks, audio
import time
from queue import SimpleQueue
from numba import njit
import matplotlib.pyplot as plt

# class Blk_mult_three(gr.sync_block):
#     def __init__(self):
#         gr.sync_block.__init__(self, name='Multiply by three', in_sig=[np.float32], out_sig=[np.float32])

#     def work(self, input_items, output_items):
#         output_items[0][0] = 3 * input_items[0][0]
#         return 1


class Blk_sink_print(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Print sink', in_sig=[np.float32], out_sig=[])

    def work(self, input_items, output_items):
        print(input_items[0][0])
        time.sleep(0.1)
        return 1


class Blk_queue_sink(gr.sync_block):
    def __init__(self, dtype, chunk_size: int):
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


def getSize(dtype):
    if dtype == np.float32:
        return gr.sizeof_float
    elif dtype == np.complex64:
        return gr.sizeof_gr_complex
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
    def __init__(self, SourceBlk: gr.gateway.gateway_block, dtype, chunk_size: int):
        self.__tb = gr.top_block()
        self.__source = SourceBlk()
        self.__stream_to_vec = blocks.stream_to_vector(getSize(dtype), chunk_size)
        self.__sink_q = Blk_queue_sink(dtype, chunk_size)
        self.__tb.connect(self.__source, self.__stream_to_vec, self.__sink_q)
        self.__tb.start()
    
    def get(self):
        return self.__sink_q.queue.get()


class Blk_source_output_arb_num(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Source: the number 213', in_sig=[], out_sig=[np.float32])
        self.i = 0

    def work(self, input_items, output_items):
        self.i += 1
        # leng = len(output_items[0])
        output_items[0][0] = self.i
        return 1


class Blk_queue_source(gr.sync_block):
    def __init__(self, dtype, chunk_size: int):
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
    def __init__(self, SinkBlk: gr.gateway.gateway_block, dtype, chunk_size: int, sink_block_args = []):
        self.__tb = gr.top_block()
        self.__source_q = Blk_queue_source(dtype, chunk_size)
        self.__vector_to_stream = blocks.vector_to_stream(getSize(dtype), chunk_size)
        self.__sink = SinkBlk(*sink_block_args)
        self.__tb.connect(self.__source_q, self.__vector_to_stream, self.__sink)
        self.__tb.start()
    
    def put(self, val):
        return self.__source_q.queue.put(val)


siz = 65536
samp_rate = 48000
qsour = QueuedSource(Blk_source_output_arb_num, np.float32, siz)
# qsink = QueuedSink(blocks.wavfile_sink, np.float32, siz, ["testf.wav", 1, samp_rate, blocks.FORMAT_WAV, blocks.FORMAT_PCM_16])
qsink = QueuedSink(audio.sink, np.float32, siz, [samp_rate])

# while True:
x = qsour.get()
seconds = x / samp_rate
y = np.sin(1000 * 2 * np.pi * seconds)
qsink.put(y)
y = np.sin(500 * 2 * np.pi * seconds)
qsink.put(y)
# plt.plot(seconds[:200], y[:200], ".")
# plt.show()

for x in range(10):
    print("waiting", x)
    time.sleep(0.5)




##################
## Ex 2 

import pcdr.sources
import pcdr.demod
import pcdr.sinks

hackrf = pcdr.sources.HackRF()
demodulator = pcdr.demod.WBFM()
audioSink = pcdr.sinks.audio()

freq = 104.3e6
while True:
    data = hackrf.get()
    audio = demodulator.process(data)
    audioSink.play(audio)
    time.sleep(2)
    hackrf.set_freq()
    freq += 0.2e6
    


