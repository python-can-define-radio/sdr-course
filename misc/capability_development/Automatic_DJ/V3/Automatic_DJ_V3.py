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


def song_info(song):
    # Need to get the correct samp rate for the song and wait time
    with contextlib.closing(wave.open(song, 'r')) as s:
        frames, song_samp_rate, = s.getnframes(), s.getframerate()
        duration = frames / float(song_samp_rate)
        return song_samp_rate, duration


def dostuff(tb, samp_rate):

    samp_rate = int(samp_rate)

    song_list = ['/home/usacys/Desktop/Paul/imperial_march.wav',
                '/home/usacys/Desktop/Paul/rebel-theme.wav',
                '/home/usacys/Desktop/Paul/what_makes_you_beautiful.wav',
                "/home/usacys/Desktop/Paul/Hell’s_Comin_with_me.wav"]

    tb.WB_Freq_Mod = analog.wfm_tx(samp_rate, samp_rate)
    
    tb.osmo_sink = osmosdr.sink()
    tb.osmo_sink.set_sample_rate(samp_rate)
    tb.osmo_sink.set_center_freq(102e6)
    tb.osmo_sink.set_gain(0)
    tb.osmo_sink.set_if_gain(20)
    

    # Steps: Wavfile Source -> Rational Resampler -> Frequency Modulation -> Osmo Sink
    #  old  # tb.connect(tb.wavfile_source, tb.rational_resampler, tb.WB_Freq_Mod, tb.osmo_sink)
    tb.connect(tb.WB_Freq_Mod, tb.osmo_sink)
    
    for song in song_list:

        song_samp_rate, duration = song_info(song)

        # Locking stops the flowgraph in place and allows you to modify things on the fly
        tb.lock()

        # Disconnect Wavfile Source and Rational Resampler
        if hasattr(tb, "wavfile_source"):
            tb.disconnect(tb.wavfile_source)
            tb.disconnect(tb.rational_resampler)
        
        # Reconfigure Wavfile Source and Rational Resampler settings
        tb.wavfile_source = blocks.wavfile_source(song)
        tb.rational_resampler = filter.rational_resampler_fff(samp_rate,song_samp_rate)

        # Reconnect everything
        tb.connect(tb.wavfile_source, tb.rational_resampler, tb.WB_Freq_Mod)

        # Unlocking the flowgraph signals to the program that the flowgraph modifications are done and ready to execute
        tb.unlock()
        time.sleep(3)

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
