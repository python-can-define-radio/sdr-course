#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: swappingtestv2
# GNU Radio version: 3.8.1.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
import contextlib
import wave



def dostuff(tb, samp_rate):
    freq_list = [2411, 2413, 2420, 2422, 2424, 2426, 2428, 2435, 2437, 2439, 2441, 2443, 2445, 2451, 2453, 2455, 2461, 2468, 2470, 2472]
    samp_rate = int(samp_rate)

    tb.file_sink = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/usacys/Desktop/Doesnt_Have_Spaces/pysdr/myfile1.data', False)
    tb.file_sink.set_unbuffered(False)

    tb.osmosdr_source = osmosdr.source(args="numchan=" + str(1) + " " + "")

    tb.osmosdr_source.set_time_unknown_pps(osmosdr.time_spec_t())
    tb.osmosdr_source.set_sample_rate(samp_rate)
    tb.osmosdr_source.set_center_freq(100e6, 0)
    tb.osmosdr_source.set_freq_corr(0, 0)
    tb.osmosdr_source.set_gain(0, 0)
    tb.osmosdr_source.set_if_gain(32, 0)
    tb.osmosdr_source.set_bb_gain(32, 0)
    tb.osmosdr_source.set_antenna('', 0)
    tb.osmosdr_source.set_bandwidth(0, 0)
    

    # Steps: Osmocom Source -> File Sink
    tb.connect((tb.osmosdr_source,0), (tb.file_sink,0))
    
    for freq in freq_list:

        # Locking stops the flowgraph in place and allows you to modify things on the fly
        tb.lock()

        # Reconfigure Osmocom Source and File Sink 

        tb.disconnect(tb.osmosdr_source, tb.file_sink)
        tb.osmosdr_source.set_center_freq(freq * 1e6, 0)
        tb.file_sink = blocks.file_sink(gr.sizeof_gr_complex*1, f'/home/usacys/Desktop/Doesnt_Have_Spaces/pysdr/{freq}.data', False)
        tb.file_sink.set_unbuffered(False)
    
        # Reconnect everything
        tb.connect((tb.osmosdr_source,0), (tb.file_sink,0))
        # Unlocking the flowgraph signals to the program that the flowgraph modifications are done and ready to execute
        tb.unlock()
        time.sleep(10)

    # input to stop program from automatically terminating
    input('Press Enter to quit')


def main():
    tb = gr.top_block()
    
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    try:
        dostuff(tb, 2e6)        
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
