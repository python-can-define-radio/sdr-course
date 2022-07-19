"""The majority of this is copy/pasted from
the bottom of a GRC-generated python file.
I added two lines."""


from distutils.version import StrictVersion
from PyQt5 import Qt
from gnuradio import gr
import sys
import signal

from threading import Thread



def set_up_qt_top_block_and_run_func_in_thread(top_block_cls, func_to_run):

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

    #######################
    ## this is my addition
    ##
    thread = Thread(target = func_to_run, args = (tb, ), daemon=True)
    thread.start()
    ## end my addition
    #######################
    qapp.exec_()