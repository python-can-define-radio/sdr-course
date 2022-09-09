#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: swappingtestv2
# GNU Radio version: 3.8.1.0

from gnuradio.analog import wfm_tx, wfm_rcv
from gnuradio import audio
from gnuradio.blocks import wavfile_source
from gnuradio.filter import rational_resampler_fff, fir_filter_ccf, firdes
from gnuradio import gr
from signal import signal, SIGINT, SIGTERM
from gnuradio.eng_arg import eng_float, intx
from sys import exit
from osmosdr import sink, source, time_spec_t
from time import sleep
from contextlib import closing
from wave import open as wopen


def song_info(song):
    # Need to get the correct samp rate for the song and wait time
    with closing(wopen(song, 'r')) as s:
        frames, song_samp_rate, = s.getnframes(), s.getframerate()
        duration = frames / float(song_samp_rate)
        return song_samp_rate, duration


def dostuff(tb, samp_rate, song):

    samp_rate = int(samp_rate)

    # receiving commands below
    tb.rational_resampler = rational_resampler_fff(interpolation=48000,decimation=int(samp_rate),taps=None,fractional_bw=None)
    
    tb.osmo_source = source(args="numchan=" + str(1) + " " + "")
   
    tb.osmo_source.set_sample_rate(samp_rate)
    tb.osmo_source.set_center_freq(102e6, 0)
    tb.osmo_source.set_if_gain(32, 0)
    tb.osmo_source.set_bb_gain(32, 0)

    
    tb.LPF = fir_filter_ccf(1,firdes.low_pass(1,samp_rate,100e3,10e3,firdes.WIN_HAMMING,6.76))
    tb.audio_sink = audio.sink(48000, '', True)
    tb.wbFDM = wfm_rcv(quad_rate=samp_rate,audio_decimation=1)



    # Order osmo_source -> LPF -> wbFDM -> rational_resampler -> audio_sink
    tb.connect(tb.osmo_source, tb.LPF, tb.wbFDM, tb.rational_resampler, tb.audio_sink)
    
    
    # Need to lock grc in place to modify it.
    tb.lock()
    
    # Need to disconnect and delete receiver
    tb.disconnect(tb.osmo_source, tb.LPF, tb.wbFDM, tb.rational_resampler, tb.audio_sink)
    del tb.osmo_source, tb.LPF, tb.wbFDM, tb.rational_resampler, tb.audio_sink




    # Transmitting commands below
    song_samp_rate, duration = song_info(song)
   

    tb.wavfile_source = wavfile_source(song)
    tb.rational_resampler = rational_resampler_fff(samp_rate,song_samp_rate)

    tb.WB_Freq_Mod = wfm_tx(samp_rate, samp_rate)
    
    tb.osmo_sink = sink()
    tb.osmo_sink.set_sample_rate(samp_rate)
    tb.osmo_sink.set_center_freq(102e6)
    tb.osmo_sink.set_gain(0)
    tb.osmo_sink.set_if_gain(50)
    

    # Steps: Wavfile Source -> Rational Resampler -> Frequency Modulation -> Osmo Sink
   
    tb.connect(tb.wavfile_source, tb.rational_resampler, tb.WB_Freq_Mod, tb.osmo_sink)

    # MAKE SURE TO UNLOCK OR IT WON'T WORK >:(
    tb.unlock()
    # sleep(duration)
    
    input('Press Enter to quit')


def main():
    song = '/home/usacys/Desktop/Paul/capabilities/imperial_march.wav'
    tb = gr.top_block()
    
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        exit(0)

    signal(SIGINT, sig_handler)
    signal(SIGTERM, sig_handler)

    tb.start()
    try:
        dostuff(tb, 2e6, song)        
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
