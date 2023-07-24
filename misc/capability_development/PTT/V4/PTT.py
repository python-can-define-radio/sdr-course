#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: swappingtestv2
# GNU Radio version: 3.8.1.0

from gnuradio.analog import wfm_tx, wfm_rcv
from gnuradio import qtgui
from gnuradio import audio
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QPushButton
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



def transmit(tb, samp_rate, song):
    samp_rate = int(samp_rate)

    if hasattr(tb, 'osmo_source'):

        # Need to lock grc in place to modify it.
        tb.lock()
        
        # Need to disconnect and delete receiver
        tb.disconnect(tb.osmo_source, tb.LPF, tb.wbFDM, tb.rational_resampler, tb.audio_sink)
        del tb.osmo_source, tb.LPF, tb.wbFDM, tb.rational_resampler, tb.audio_sink
        tb.tracker = 'exists'

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
    if hasattr(tb, 'tracker'):
        tb.unlock()

    # sleep(duration)

def receive(tb, samp_rate):
    samp_rate = int(samp_rate)
    # receiving commands below
    
    if hasattr(tb, 'osmo_sink'):
        tb.lock()
        tb.disconnect(tb.wavfile_source, tb.rational_resampler, tb.WB_Freq_Mod, tb.osmo_sink)
        del tb.wavfile_source, tb.rational_resampler, tb.WB_Freq_Mod, tb.osmo_sink
        tb.tracker = 'exists'

    tb.rational_resampler = rational_resampler_fff(interpolation=48000,decimation=int(samp_rate),taps=None,fractional_bw=None)
    
    tb.osmo_source = source(args="numchan=" + str(1) + " " + "")
   
    tb.osmo_source.set_sample_rate(samp_rate)
    tb.osmo_source.set_center_freq(102e6, 0)
    tb.osmo_source.set_if_gain(32, 0)
    tb.osmo_source.set_bb_gain(32, 0)

    
    tb.LPF = fir_filter_ccf(1,firdes.low_pass(1,samp_rate,100e3,10e3,firdes.WIN_HAMMING,6.76))
    tb.audio_sink = audio.sink(48000, '', True)
    tb.wbFDM = wfm_rcv(quad_rate=samp_rate,audio_decimation=1)

    if hasattr(tb, 'tracker'):
        tb.unlock()

    # Order osmo_source -> LPF -> wbFDM -> rational_resampler -> audio_sink
    tb.connect(tb.osmo_source, tb.LPF, tb.wbFDM, tb.rational_resampler, tb.audio_sink)


def dostuff(tb, samp_rate, song):
    samp_rate = int(samp_rate)
    # qtgui.util.check_set_qss()
    # myapp = QApplication([])
    # try:
    #     tb.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
    # except:
    #     pass
    # tb.top_scroll_layout = Qt.QVBoxLayout()
 
    # tb.top_scroll = Qt.QScrollArea()
    # tb.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
    # tb.top_scroll_layout.addWidget(tb.top_scroll)
    # tb.top_scroll.setWidgetResizable(True)
    # tb.top_widget = Qt.QWidget()
    # tb.top_scroll.setWidget(tb.top_widget)
    # tb.top_layout = Qt.QVBoxLayout(tb.top_widget)
    tb.top_grid_layout = Qt.QGridLayout()
    # tb.top_layout.addLayout(tb.top_grid_layout)
   
    myapp = QApplication([])
    _signal_power_push_button = QPushButton('')
    _signal_power_push_button = QPushButton('signal_power')
    tb._signal_power_choices = {'Pressed': transmit(tb, samp_rate, song), 'Released': receive(tb, samp_rate)}
    _signal_power_push_button.pressed.connect(lambda: tb.set_signal_power(tb._signal_power_choices['Pressed']))
    _signal_power_push_button.released.connect(lambda: tb.set_signal_power(tb._signal_power_choices['Released']))
    tb.top_grid_layout.addWidget(_signal_power_push_button)

    samp_rate = int(samp_rate)

    
    
    
    
    
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
