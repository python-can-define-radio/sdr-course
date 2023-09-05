from gnuradio import gr, blocks
import pmt
import numpy as np
import osmosdr
from typing import List, Protocol
import deal

from pcdr.our_GR_blocks import queue_sink




## Bizarre GNU Radio variable-rename issues

_osmocom_source_to_queuequeue_sink = queue_sink



class osmocom_source_to_queue_sink(gr.top_block):

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

        self.queue_sink = queue_sink(chunk_size)

        self.connect(self.osmosdr_source, self.blocks_stream_to_vector, self.queue_sink)

    
class file_source_to_queue_sink(gr.top_block):

    def __init__(self, filename: str, chunk_size: int, repeat: bool):
        gr.top_block.__init__(self, "Top block")
        self.__chunk_size = chunk_size
        self.file_source = blocks.file_source(gr.sizeof_gr_complex, filename, repeat)
        self.file_source.set_begin_tag(pmt.PMT_NIL)  # Don't know if this is needed
        self.blocks_stream_to_vector = blocks.stream_to_vector(gr.sizeof_gr_complex, chunk_size)
        self.queue_sink = queue_sink(chunk_size)
        self.connect(self.file_source, self.blocks_stream_to_vector, self.queue_sink)



