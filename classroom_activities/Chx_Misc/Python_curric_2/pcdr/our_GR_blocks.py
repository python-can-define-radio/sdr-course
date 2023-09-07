import numpy as np
from gnuradio import gr
from gnuradio import blocks
import osmosdr
import time
from queue import Empty
from pcdr.helpers import SimpleQueueTypeWrapped, queue_to_list
from queue import Full
from typing import List
import deal


class queue_source(gr.sync_block):

    @deal.pre(lambda _: _.external_queue.qtype == np.ndarray)
    @deal.pre(lambda _: _.external_queue.dtype == _.out_type)
    @deal.pre(lambda _: _.external_queue.chunk_size == _.chunk_size)
    def __init__(self, external_queue: SimpleQueueTypeWrapped, chunk_size: int, out_type = np.complex64):
        gr.sync_block.__init__(
            self,
            name='Python Block: Queue Source',
            in_sig=[],
            out_sig=[(out_type, chunk_size)]
        )
        self.__queue = external_queue
        self.__chunk_size = chunk_size


    def work(self, input_items, output_items):
        try:
            output_items[0][0][:] = self.__queue.get_nowait()
            return 1
        except Empty:
            return -1  # Block is done
    
    
    @deal.pre(lambda _: len(_.data) == _.self.__chunk_size)
    def queue_put(self, data):
        self.__queue.put(data)


class print_sink(gr.sync_block):

    def __init__(self, sleep_seconds=0.5):
        gr.sync_block.__init__(
            self,
            name="Python Block: Print",
            in_sig=[np.complex64],
            out_sig=[]
        )
        self.sleep_seconds = sleep_seconds
        
    def work(self, input_items, output_items):
        singleDataPoint = input_items[0][0]

        print(singleDataPoint)
        time.sleep(self.sleep_seconds)

        return 1


class string_file_sink(gr.sync_block):

    def __init__(self, filename):
        gr.sync_block.__init__(
            self,
            name="Python Block: String File Sink",
            in_sig=[np.complex64],
            out_sig=[]
        )
        self.f = open(filename, "w")
        
    def work(self, input_items, output_items):
        singleDataPoint = input_items[0][0]

        self.f.write(f"{singleDataPoint}, ")
        self.f.flush()

        return 1


class queue_sink(gr.sync_block):

    def __init__(self, chunk_size: int):
        gr.sync_block.__init__(
            self,
            name='Python Block: Data Queue Sink',
            in_sig=[(np.complex64, chunk_size)],
            out_sig=[]
        )
        self.__queue = SimpleQueueTypeWrapped(np.ndarray, np.complex64, chunk_size)
        self.__chunk_size = chunk_size


    def work(self, input_items, output_items):
        datacopy = input_items[0][0].copy()
        self.__queue.put(datacopy)
        return 1


    @deal.ensure(lambda _: len(_.result) == _.self.__chunk_size)
    def get(self) -> np.ndarray:
        """Get a chunk from the queue of accumulated received data."""
        return self.__queue.get()

    def get_all(self) -> List[np.ndarray]:
        """Warning: this may or may not work while the flowgraph is running."""
        return queue_to_list(self.__queue)


