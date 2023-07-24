#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: swappingtestv2
# GNU Radio version: 3.8.1.0

from gnuradio.analog import wfm_tx
from gnuradio.blocks import wavfile_source
from gnuradio.filter import rational_resampler_fff
from gnuradio import gr
from signal import signal, SIGINT, SIGTERM
from gnuradio.eng_arg import eng_float, intx
from sys import exit
from osmosdr import sink
from time import sleep
from contextlib import closing
from wave import open as wopen


def song_info(song):
    # Need to get the correct samp rate for the song and wait time
    with closing(wopen(song, 'r')) as s:
        frames, song_samp_rate, = s.getnframes(), s.getframerate()
        duration = frames / float(song_samp_rate)
        return song_samp_rate, duration


def dostuff(tb, samp_rate):

    samp_rate = int(samp_rate)

    song_list = ['/home/usacys/Desktop/Paul/imperial_march.wav',
                '/home/usacys/Desktop/Paul/rebel-theme.wav',
                '/home/usacys/Desktop/Paul/what_makes_you_beautiful.wav',
                "/home/usacys/Desktop/Paul/Hell’s_Comin_with_me.wav"]

    tb.WB_Freq_Mod = wfm_tx(samp_rate, samp_rate)
    
    tb.osmo_sink = sink()
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
        tb.wavfile_source = wavfile_source(song)
        tb.rational_resampler = rational_resampler_fff(samp_rate,song_samp_rate)

        # Reconnect everything
        tb.connect(tb.wavfile_source, tb.rational_resampler, tb.WB_Freq_Mod)

        # Unlocking the flowgraph signals to the program that the flowgraph modifications are done and ready to execute
        tb.unlock()
        sleep(3)

    # input to stop program from automatically terminating
    input('Press Enter to quit')


def main():
    tb = gr.top_block()
    
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        exit(0)

    signal(SIGINT, sig_handler)
    signal(SIGTERM, sig_handler)

    tb.start()
    try:
        dostuff(tb, 2e6)        
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
