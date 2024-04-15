"""
Commandline functionality for displaying signal data in the terminal using
the dashing module built on blessed.
https://github.com/FedericoCeratto/dashing
"""

from __future__ import annotations
from gnuradio import gr
from gnuradio import blocks
import time
import numpy as np
import sys
import signal
from dashing import HChart



def configure_exit_signal(tb: gr.top_block):
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


class dashing_display(gr.sync_block):

    def __init__(self, sleep_seconds=1.0/90):
        gr.sync_block.__init__(
            self,
            name="Print block",
            in_sig=[np.complex64],
            out_sig=[]
        )
        self.ui = HChart(title="Some Horizontal Chart", color=7, border_color=2)
        self.sleep_seconds = sleep_seconds

    def work(self, input_items, output_items):
        singleDataPoint = input_items[0][0]
        self.ui.append(singleDataPoint)
        self.ui.display()
        time.sleep(self.sleep_seconds)
        return 1

class Random_Signal_Generator(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "Top block")
        d = np.array([2, 10, 50], dtype=np.complex64)
        self.myFirstBlock = blocks.vector_source_c(d, repeat=True)
        self.dashing_display = dashing_display()
        self.connect(self.myFirstBlock, self.dashing_display)

tb = Random_Signal_Generator()
configure_exit_signal(tb)
tb.start()
while True:
    time.sleep(0.25)

