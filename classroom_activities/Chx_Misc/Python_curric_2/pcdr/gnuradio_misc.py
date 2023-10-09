from gnuradio import gr
import sys
import signal
from distutils.version import StrictVersion



def configure_graceful_exit(tb: gr.top_block):
    """The portion of GNU Radio boilerplate that 
    catches SIGINT and SIGTERM, and tells the flowgraph
    to gracefully stop before exiting the program.
    
    Used mainly for non-graphical flowgraphs."""
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)


try:
    ## Why this import is here:
    ## We don't want Qt to be required for ALL pcdr uses;
    ## just graphical ones.
    from PyQt5 import Qt

    # class tb_qt_widget_type(gr.top_block, Qt.QWidget):
    #     pass


    def configure_and_run_gui_flowgraph(top_block_cls, args):
        """The portion of GNU Radio boilerplate that 
        sets up the QT GUI Application."""
        if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        qapp = Qt.QApplication(sys.argv)

        tb = top_block_cls(*args)
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

except ModuleNotFoundError:
    print("WARNING: Did not find PyQt5. QT-related GUIs will be unavailable.")
