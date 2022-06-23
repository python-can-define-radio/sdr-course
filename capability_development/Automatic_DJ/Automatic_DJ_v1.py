#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: swappingtest
# GNU Radio version: 3.8.1.0

"""This is a proof of concept python file. 
The important lines here are lines 41-52 and lines 143-157. 
These are the lines that update the counter in this instance of the swapping test class.
By using the .set_input_index() method we are able to create a program that automatically 
swaps between a list of songs."""




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
import wave
import contextlib


class swappingtest(gr.top_block):
    count = 0
    song_list = ['/home/usacys/Desktop/Paul/imperial_march.wav', '/home/usacys/Desktop/Paul/rebel-theme.wav']
    duration = 0
    
    def gettime(self, songlist):
        with contextlib.closing(wave.open(songlist[self.count], 'r')) as song:
            seconds = song.getnframes()
            song_sr = song.getframerate()
            self.duration = seconds / float(song_sr)
        return self.duration 

    def counter(self, item):
        self.count += 1
        if self.count >= len(item) - 1:
            self.count = len(item) - 1
            return self.count

    def __init__(self):
        gr.top_block.__init__(self, "swappingtest")
        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6

        ##################################################
        # Blocks
        ##################################################
        # pdb.set_trace()
        
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=int(samp_rate),
                decimation=44100,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(samp_rate),
                decimation=22050,
                taps=None,
                fractional_bw=None)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(102e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/usacys/Desktop/Paul/imperial_march.wav', False)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/home/usacys/Desktop/Paul/rebel-theme.wav', False)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,self.count,0)
        # self.blocks_selector_0.set_enabled(False)
        self.analog_wfm_tx_0_0 = analog.wfm_tx(
        	audio_rate=int(samp_rate),
        	quad_rate=int(samp_rate),
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=int(samp_rate),
        	quad_rate=int(samp_rate),
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.analog_wfm_tx_0_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_selector_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_tx_0_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)



def main(top_block_cls=swappingtest, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    try:
        
        tb.counter(tb.song_list)
        print(tb.count)
        # tb.blocks_selector_0.set_enabled(True)
        tb.blocks_selector_0.set_input_index(0)
        x = input('Press Enter to quit: ')
            

    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
