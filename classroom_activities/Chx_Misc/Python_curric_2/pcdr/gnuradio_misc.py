from __future__ import annotations
from gnuradio import gr
import sys
import signal



def configure_graceful_exit(tb: gr.top_block):
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)