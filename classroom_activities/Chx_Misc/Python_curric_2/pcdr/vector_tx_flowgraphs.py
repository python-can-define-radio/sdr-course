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
from pcdr.our_GR_blocks import print_sink, string_file_sink
from gnuradio import zeromq
from typing import Tuple
from pcdr.helpers import validate_hack_rf_transmit


## Bizarre GNU Radio variable-rename issues

# _queue_to_print_sink__queue_source = queue_source
# _queue_to_string_file_sink__queue_source = queue_source
# _queue_to_osmocom_sink__queue_source = queue_source
# _queue_to_string_file_sink__string_file_sink = string_file_sink
# _queue_to_print_sink__print_sink = print_sink
# _queue_to_zmqpub_sink__queue_source = queue_source


class vector_to_osmocom_sink(gr.top_block):

    def __init__(self,
                 data: Tuple[complex],
                 center_freq: float,
                 samp_rate: float,
                 if_gain: int,
                 device_args: str,
                 repeat: bool):
        """device_args: "hackrf=0" is common."""
        
        validate_hack_rf_transmit(samp_rate, center_freq, if_gain)

        gr.top_block.__init__(self, "Top block")
        
        self.vector_source = blocks.vector_source_c(data, repeat)

        self.osmosdr_sink = osmosdr.sink(args=device_args)
        self.osmosdr_sink.set_sample_rate(samp_rate)
        self.osmosdr_sink.set_center_freq(center_freq)
        self.osmosdr_sink.set_gain(0)
        self.osmosdr_sink.set_if_gain(if_gain)
        self.osmosdr_sink.set_bb_gain(0)

        self.connect(self.vector_source, self.osmosdr_sink)


class vector_to_print_sink(gr.top_block):
    def __init__(self, print_delay: float, data: Tuple[complex], repeat: bool):
        gr.top_block.__init__(self, "Top block")
        self.vector_source = blocks.vector_source_c(data, repeat)
        self.print_sink = print_sink(print_delay)
        self.connect(self.vector_source, self.print_sink)


class vector_to_string_file_sink(gr.top_block):
    def __init__(self, filename: str, data: Tuple[complex]):
        assert isinstance(filename, str)
        gr.top_block.__init__(self, "Top block")
        self.vector_source = blocks.vector_source_c(data)
        self.string_file_sink = string_file_sink(filename)
        self.connect(self.vector_source, self.string_file_sink)


class vector_to_file_sink(gr.top_block):
    def __init__(self, data: Tuple[complex], filename: str):
        assert isinstance(filename, str)
        gr.top_block.__init__(self, "Top block")
        self.vector_source = blocks.vector_source_c(data)
        self.file_sink = blocks.file_sink(gr.sizeof_gr_complex, filename, append=False)
        self.file_sink.set_unbuffered(False)
        self.connect(self.vector_source, self.file_sink)


class vector_to_zmqpub_sink(gr.top_block):
    """UNTESTED"""
    def __init__(self, port: int, data: np.ndarray, repeat: bool):
        gr.top_block.__init__(self, "Top block")
        self.vector_source = blocks.vector_source_c(data, repeat)
        self.zmqpub_sink = zeromq.pub_sink(gr.sizeof_gr_complex, 1, f'tcp://0.0.0.0:{port}', 100, False, -1)
        self.connect(self.vector_source, self.zmqpub_sink)
        
        