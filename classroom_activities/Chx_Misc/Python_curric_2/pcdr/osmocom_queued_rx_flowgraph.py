from gnuradio import gr, blocks
import numpy as np
import time
import osmosdr
from queue import SimpleQueue, Empty

class osmocom_source_to_queue(gr.top_block):
    def __init__(self, center_freq: float, samp_rate: float, device_args: str, if_gain: int = 16, bb_gain: int = 50):
        gr.top_block.__init__(self, "Top block")
        self.osmosdr_source = osmosdr.source(args=device_args)
        self.osmosdr_source.set_sample_rate(samp_rate)
        self.osmosdr_source.set_center_freq(center_freq)
        self.osmosdr_source.set_gain(0)
        self.osmosdr_source.set_if_gain(if_gain)
        self.osmosdr_source.set_bb_gain(bb_gain)
        self.osmosdr_source.set_bandwidth(0)
        self.blocks_stream_to_vector = blocks.stream_to_vector(gr.sizeof_gr_complex, 1024)
        self.blocks_null_sink = blocks.null_sink(gr.sizeof_gr_complex*1024)

        self.connect(self.osmosdr_source, self.blocks_stream_to_vector, self.blocks_null_sink)