import numpy as np
from gnuradio import gr
from gnuradio import blocks
import osmosdr
import time
from queue import Empty
from pcdr.helpers import SimpleQueueTypeWrapped
import deal


class __data_queue_source(gr.sync_block):

    @deal.pre(lambda _: _.external_queue.qtype == _.out_type)
    def __init__(self, external_queue: SimpleQueueTypeWrapped, chunk_size: int, out_type = np.complex64):
        gr.sync_block.__init__(
            self,
            name='Python Block: Data Queue Source',
            in_sig=[],
            out_sig=[(out_type, chunk_size)]
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