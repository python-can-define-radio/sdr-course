from gnuradio import gr, blocks
import pmt
import numpy as np
import osmosdr
from typing import List, Protocol

from pcdr.our_GR_blocks import queue_sink
from pcdr.helpers import validate_hack_rf_receive




## Bizarre GNU Radio variable-rename issues

_osmocom_source_to_queuequeue_sink = queue_sink



class osmocom_source_to_queue_sink(gr.top_block):

    
    def __init__(self, center_freq: float, samp_rate: float, chunk_size: int, device_args: str, if_gain: int = 32, bb_gain: int = 42):
        gr.top_block.__init__(self, "Top block")

        ## TODO: This should be device_name instead of device_args.
        validate_hack_rf_receive(device_args, samp_rate, center_freq, if_gain, bb_gain)
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



