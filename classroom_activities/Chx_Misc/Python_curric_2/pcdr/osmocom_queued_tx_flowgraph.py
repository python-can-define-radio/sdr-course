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
            in_sig=[np.complex64],
            out_sig=[]
        )
        self.sleep_seconds = sleep_seconds
        
    def work(self, input_items, output_items):
        singleDataPoint = input_items[0][0]

        print(singleDataPoint)
        time.sleep(self.sleep_seconds)

        return 1


class __string_file_sink(gr.sync_block):

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


class __data_queue_source(gr.sync_block):

    def __init__(self, external_queue):
        gr.sync_block.__init__(
            self,
            name='Python Block: Data Queue Source',
            in_sig=[],
            out_sig=[(np.complex64, 1024)]
        )
        if external_queue == None:
            self.__data_queue = queue.SimpleQueue()
        else:
            self.__data_queue = external_queue

    def work(self, input_items, output_items):
        output_items[0][0] = self.__data_queue.get()
        return 1
    
    def queue_put(self, data):
        if len(data) != 1024:
            raise ValueError("Data must be 1024 items long")
        self.__data_queue.put(data)


## Bizarre GNU Radio variable-rename issues

_queue_to__print_blk__data_queue_source = __data_queue_source
_queue_to__string_file_sink__data_queue_source = __data_queue_source
_queue_to__osmocom_sink__data_queue_source = __data_queue_source
_queue_to__string_file_sink__string_file_sink = __string_file_sink
_queue_to__print_blk__print_blk = __print_blk

class queue_to__osmocom_sink(gr.top_block):

    def __init__(self, center_freq, samp_rate, if_gain=24, external_queue=None):
        gr.top_block.__init__(self, "Top block")

        self.samp_rate = samp_rate
        
        self.data_queue_source = __data_queue_source(external_queue)

        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, 1024)

        self.osmosdr_sink = osmosdr.sink()
        self.osmosdr_sink.set_sample_rate(samp_rate)
        self.osmosdr_sink.set_center_freq(center_freq)
        self.osmosdr_sink.set_gain(0)
        self.osmosdr_sink.set_if_gain(if_gain)
        self.osmosdr_sink.set_bb_gain(0)

        self.connect(self.data_queue_source, self.vector_to_stream, self.osmosdr_sink)


class queue_to__print_blk(gr.top_block):

    def __init__(self, print_delay=0.5, external_queue=None):
        gr.top_block.__init__(self, "Top block")
        self.data_queue_source = __data_queue_source(external_queue)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, 1024)
        self.print_blk = __print_blk(print_delay)
        self.connect(self.data_queue_source, self.vector_to_stream, self.print_blk)


class queue_to__string_file_sink(gr.top_block):

    def __init__(self, filename, external_queue=None):
        gr.top_block.__init__(self, "Top block")
        self.data_queue_source = __data_queue_source(external_queue)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, 1024)
        self.string_file_sink = __string_file_sink(filename)
        self.connect(self.data_queue_source, self.vector_to_stream, self.string_file_sink)


class top_block_manager():

    def __init__(self, tb):
        self.tb = tb
        def sig_handler(sig=None, frame=None):
            tb.stop()
            tb.wait()
            sys.exit(0)

        signal.signal(signal.SIGINT, sig_handler)
        signal.signal(signal.SIGTERM, sig_handler)

    def start(self):
        self.tb.start()    
    
    def start_and_keep_open(self, seconds):
        self.start()
        time.sleep(seconds)


def send_data(dat, center_freq, seconds_to_wait_till_finished=1.0):
    
    tb = queue_to__osmocom_sink(center_freq)
    for datpiece in dat:
        tb.data_queue_source.queue_put(datpiece)
    tbm = top_block_manager(tb)
    tbm.start_and_keep_open(seconds=seconds_to_wait_till_finished)
    
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    dat = np.ones(1024)
    dat[0] = 0.3
    send_data(dat, 101e6)
    
