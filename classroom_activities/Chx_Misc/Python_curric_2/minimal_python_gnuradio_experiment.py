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



class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Python Block: Gen Rand Data',   # will show up in GRC
            in_sig=[],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        the_only_output_port = output_items[0]
        leng = len(the_only_output_port)  # pretend this is 4
        randdat = np.random.uniform(0, 1, leng)
        ######################################
        ## Don't do this
        the_only_output_port = randdat

        ## Do this
        the_only_output_port[:] = randdat

        print("Finished running work; sleeping 3 seconds.")
        time.sleep(3)
        return leng


class my_top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6

        ##################################################
        # Blocks
        ##################################################
        self.epy_block = blk()

        # self.osmosdr_sink = osmosdr.sink()
        # self.osmosdr_sink.set_sample_rate(samp_rate)
        # self.osmosdr_sink.set_center_freq(101e6)
        # self.osmosdr_sink.set_gain(0)
        # self.osmosdr_sink.set_if_gain(24)
        # self.osmosdr_sink.set_bb_gain(32)

        ## can use this null sink instead of the osmocom for debugging
        self.null_sink = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.connect(self.epy_block, self.null_sink)



def main():
    tb = my_top_block()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
