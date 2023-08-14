from __future__ import annotations
from gnuradio import gr, blocks
import numpy as np
import time
import random
import osmosdr
from queue import SimpleQueue, Empty, Full
import deal

from pcdr.modulators import ook_modulate
from pcdr.wavegen import createTimestamps, makeRealWave
from pcdr.helpers import queue_to_list



class __data_queue_sink(gr.sync_block):

    def __init__(self, chunk_size: int):
        gr.sync_block.__init__(
            self,
            name='Python Block: Data Queue Sink',
            in_sig=[(np.complex64, chunk_size)],
            out_sig=[]
        )
        self.__data_queue = SimpleQueue()
        self.__chunk_size = chunk_size


    def work(self, input_items, output_items):
        try:
            datacopy = input_items[0][0].copy()
            self.__data_queue.put(datacopy)
            return 1
        except Full:
            print("Queue Full")


    @deal.ensure(lambda _: len(_.result) == _.self.__chunk_size)
    def queue_get(self) -> np.ndarray:
        """Get a chunk from the queue of accumulated received data."""
        return self.__data_queue.get()

    def queue_get_all(self) -> list[np.ndarray]:
        """Warning: this may or may not work while the flowgraph is running."""
        return queue_to_list(self.__data_queue)
        


## Bizarre GNU Radio variable-rename issues

_osmocom_source_to_queue__data_queue_sink = __data_queue_sink


class osmocom_source_to_queue(gr.top_block):
    
    @deal.pre(lambda _: 1e6 <= _.center_freq <= 6e9)
    @deal.pre(lambda _: 2e6 <= _.samp_rate <= 20e6)
    @deal.pre(lambda _: _.if_gain in [0, 8, 16, 24, 32, 40])
    @deal.pre(lambda _: _.bb_gain in range(0, 62+1, 2), message="bb_gain must be one of 0, 2, 4, 6, ... 58, 60, 62")
    def __init__(self, center_freq: float, samp_rate: float, chunk_size: int, device_args: str, if_gain: int = 32, bb_gain: int = 42):
        gr.top_block.__init__(self, "Top block")

        self.__chunk_size = chunk_size

        self.osmosdr_source = osmosdr.source(args=device_args)
        self.osmosdr_source.set_sample_rate(samp_rate)
        self.osmosdr_source.set_center_freq(center_freq)
        self.osmosdr_source.set_gain(0)
        self.osmosdr_source.set_if_gain(if_gain)
        self.osmosdr_source.set_bb_gain(bb_gain)

        self.blocks_stream_to_vector = blocks.stream_to_vector(gr.sizeof_gr_complex, chunk_size)

        self.data_queue_sink = __data_queue_sink(chunk_size)

        self.connect(self.osmosdr_source, self.blocks_stream_to_vector, self.data_queue_sink)


    @deal.ensure(lambda _: len(_.result) == _.self.__chunk_size)
    def get(self) -> np.ndarray:
        """Get a chunk from the queue of accumulated received data."""
        return self.data_queue_sink.queue_get()
    
    def get_all(self) -> list[np.ndarray]:
        """Warning: this may or may not work while the flowgraph is running."""
        return self.data_queue_sink.queue_get_all()


class simulated_data_to_queue(gr.top_block):
    def __init__(self, samp_rate: float):
        modded = ook_modulate(data=[1, 0, 1, 0, 1, 0, 1, 1], bit_length=25)
        t = len(modded) / samp_rate
        timestamps = createTimestamps(seconds=t, num_samples=len(modded))
        wave = makeRealWave(timestamps, freq=4)
        fully_modded = modded * wave
        including_initial_empty = np.concatenate(
            [np.zeros(random.randint(100, 500)), fully_modded]
        )
        noisy = including_initial_empty + np.random.normal(len(including_initial_empty))
        # TODO:
        # fakeQueue = pad_chunk_queue(TODO, arbitrary_size)
        raise NotImplementedError()
        
