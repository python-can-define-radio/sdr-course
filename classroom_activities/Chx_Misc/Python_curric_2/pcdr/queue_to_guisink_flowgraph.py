#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.8.1.0



from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import qtgui
from pcdr.helpers import SimpleQueueTypeWrapped
from pcdr.our_GR_blocks import queue_source
from pcdr.wrapped_GR_blocks import qt_gui_init_boilerplate



_queue_to_guisink__queue_source = queue_source

class queue_to_guisink(gr.top_block, Qt.QWidget):

    def __init__(self, center_freq: float, samp_rate: float, external_queue: SimpleQueueTypeWrapped, chunk_size: int):
        gr.top_block.__init__(self, "Not titled yet")
        qt_gui_init_boilerplate(self, "queue_to_guisink")
        
        ##################################################
        # Blocks
        ##################################################
        self.queue_source = queue_source(external_queue, chunk_size)
        self.vector_to_stream = blocks.vector_to_stream(gr.sizeof_gr_complex, chunk_size)
        self.blocks_throttle = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)
        self.qtgui_sink = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_HARRIS, #wintype    # In GR 3.10.7, this is gnuradio.fft.window.WIN_BLACKMAN_HARRIS
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink.set_update_time(1.0/10)
        self._qtgui_sink_win = sip.wrapinstance(self.qtgui_sink.pyqwidget(), Qt.QWidget)

        self.qtgui_sink.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_win)
        



        ##################################################
        # Connections
        ##################################################
        self.connect(self.queue_source, self.vector_to_stream, self.blocks_throttle, self.qtgui_sink)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "queue_to_guisink")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

