#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PTT_test
# Author: usacys
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
from gnuradio import qtgui

class PTT_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "PTT_test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("PTT_test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "PTT_test")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source(args="numchan=" + str(1) + " " + "")
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(100e6, 0)
        self.osmosdr_source_0.set_if_gain(28, 0)
                
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.connect((self.osmosdr_source_0, 0), (self.blocks_null_sink_0, 0))
        
        
        self.lock()


        self.disconnect((self.osmosdr_source_0, 0), (self.blocks_null_sink_0, 0))

        del self.osmosdr_source_0
        del self.blocks_null_sink_0

        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)
        self.osmosdr_sink_0 = osmosdr.sink(args="numchan=" + str(1) + " " + "")
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(100e6, 0)
        self.osmosdr_sink_0.set_if_gain(28, 0)

        self.connect((self.analog_noise_source_x_0, 0), (self.osmosdr_sink_0, 0))
       
        self.unlock()
       




        ##################################################
        # Connections
        ##################################################
        

       

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PTT_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)



def main(top_block_cls=PTT_test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
