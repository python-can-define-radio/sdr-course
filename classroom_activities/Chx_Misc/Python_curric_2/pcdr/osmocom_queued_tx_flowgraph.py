#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Osmocom helper
# GNU Radio version: 3.8.1.0

import numpy as np
from gnuradio import gr
from gnuradio import blocks
import osmosdr
import time
from queue import SimpleQueue, Empty
from pcdr.our_GR_blocks import queue_source, string_file_sink, print_sink
from pcdr.helpers import validate_hack_rf_transmit
from gnuradio import zeromq




## Bizarre GNU Radio variable-rename issues

_queue_to_print_sink__queue_source = queue_source
_queue_to_string_file_sink__queue_source = queue_source
_queue_to_osmocom_sink__queue_source = queue_source
_queue_to_string_file_sink__string_file_sink = string_file_sink
_queue_to_print_sink__print_sink = print_sink
_queue_to_zmqpub_sink__queue_source = queue_source


class queue_to_osmocom_sink(gr.top_block):

    def __init__(self,
                 center_freq: float,
                 samp_rate: float,
                 chunk_size: int,
                 if_gain: int,
                 external_queue: SimpleQueue,
                 device_args: str = "hackrf=0"):
        
        gr.top_block.__init__(self, "Top block")
        
        validate_hack_rf_transmit(samp_rate, center_freq, if_gain)

        self.queue_source = queue_source(external_queue, chunk_size)

        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, chunk_size)

        self.osmosdr_sink = osmosdr.sink(args=device_args)
        self.osmosdr_sink.set_sample_rate(samp_rate)
        self.osmosdr_sink.set_center_freq(center_freq)
        self.osmosdr_sink.set_gain(0)
        self.osmosdr_sink.set_if_gain(if_gain)
        self.osmosdr_sink.set_bb_gain(0)

        self.connect(self.queue_source, self.vector_to_stream, self.osmosdr_sink)


class queue_to_print_sink(gr.top_block):

    def __init__(self, print_delay: float, external_queue: SimpleQueue, chunk_size: int):
        gr.top_block.__init__(self, "Top block")
        self.queue_source = queue_source(external_queue, chunk_size)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, chunk_size)
        self.print_sink = print_sink(print_delay)
        self.connect(self.queue_source, self.vector_to_stream, self.print_sink)


class queue_to_string_file_sink(gr.top_block):

    def __init__(self, filename: str, external_queue: SimpleQueue, chunk_size: int):
        gr.top_block.__init__(self, "Top block")
        self.queue_source = queue_source(external_queue, chunk_size)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, chunk_size)
        self.string_file_sink = string_file_sink(filename)
        self.connect(self.queue_source, self.vector_to_stream, self.string_file_sink)


class queue_to_file_sink(gr.top_block):

    def __init__(self, filename: str, external_queue: SimpleQueue, chunk_size: int):
        gr.top_block.__init__(self, "Top block")
        self.queue_source = queue_source(external_queue, chunk_size)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, chunk_size)
        self.file_sink = blocks.file_sink(gr.sizeof_gr_complex, filename, append=False)
        self.file_sink.set_unbuffered(False)
        self.connect(self.queue_source, self.vector_to_stream, self.file_sink)


class queue_to_zmqpub_sink(gr.top_block):

    def __init__(self, port: int, external_queue: SimpleQueue, chunk_size: int):
        gr.top_block.__init__(self, "Top block")
        self.queue_source = queue_source(external_queue, chunk_size)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, chunk_size)
        self.zmqpub_sink = zeromq.pub_sink(gr.sizeof_gr_complex, 1, f'tcp://0.0.0.0:{port}', 100, False, -1)
        self.connect(self.queue_source, self.vector_to_stream, self.zmqpub_sink)
        
        