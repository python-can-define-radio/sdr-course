from __future__ import annotations
import numpy as np
from gnuradio import gr
from gnuradio import blocks
import osmosdr
import time
from queue import SimpleQueue, Empty
import deal


class __data_queue_source(gr.sync_block):

    def __init__(self, external_queue: SimpleQueue[np.ndarray], chunk_size: int):
        gr.sync_block.__init__(
            self,
            name='Python Block: Data Queue Source',
            in_sig=[],
            out_sig=[(np.complex64, chunk_size)]
        )
        self.__data_queue = external_queue
        self.__chunk_size = chunk_size


    def work(self, input_items, output_items):
        try:
            output_items[0][0] = self.__data_queue.get_nowait()
            return 1
        except Empty:
            return -1  # Block is done
    
    
    @deal.pre(lambda _: len(_.data) == _.self.__chunk_size)
    def queue_put(self, data):
        self.__data_queue.put(data)