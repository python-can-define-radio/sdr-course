#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.8.1.0

import numpy as np
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio import blocks
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
import queue

class __print_blk(gr.sync_block):

    def __init__(self, sleep_seconds=0.5):
        gr.sync_block.__init__(
            self,
            name="Python Block: Print",
            in_sig=[(np.complex64, 1024)],
            out_sig=[]
        )
        self.sleep_seconds = sleep_seconds
        
    def work(self, input_items, output_items):
        singleDataPoint = input_items[0][0]

        print(singleDataPoint)
        # print("{:.3f}".format(singleDataPoint))
        time.sleep(self.sleep_seconds)

        return 1

class __data_queue_source(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Python Block: do something',
            in_sig=[],
            out_sig=[(np.complex64, 1024)]
        )
        self.data_queue = queue.SimpleQueue()

    def work(self, input_items, output_items):
        output_items[0][0] = self.data_queue.get()
        return 1
    
    def queue_put(self, data):
        if len(data) != 1024:
            raise ValueError("Data must be 1024 items long")
        self.data_queue.put(data)


## Bizarre GNU Radio variable-rename issues
_my_top_block__data_queue_source = __data_queue_source


class __my_top_block(gr.top_block):

    def __init__(self, center_freq):
        gr.top_block.__init__(self, "Top block")

        self.samp_rate = samp_rate = 8e6
        
        self.data_queue_source = __data_queue_source()

        self.osmosdr_sink = osmosdr.sink()
        self.osmosdr_sink.set_sample_rate(samp_rate)
        self.osmosdr_sink.set_center_freq(center_freq)
        self.osmosdr_sink.set_gain(0)
        self.osmosdr_sink.set_if_gain(24)
        self.osmosdr_sink.set_bb_gain(32)
    
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, 1024)

        self.connect(self.data_queue_source, self.vector_to_stream, self.osmosdr_sink)


def send_data(dat, center_freq, seconds_to_wait_till_finished=1.0):
    tb = __my_top_block(center_freq)

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    for datpiece in dat:
        tb.data_queue_source.queue_put(datpiece)
    time.sleep(seconds_to_wait_till_finished)
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    dat = np.ones(1024)
    dat[0] = 0.3
    send_data(dat, 101e6)
    
