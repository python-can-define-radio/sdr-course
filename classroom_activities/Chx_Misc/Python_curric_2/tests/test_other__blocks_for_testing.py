from gnuradio import gr
import numpy as np


class Blk_mult_three(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Multiply by three', in_sig=[np.uint8], out_sig=[np.float32])

    def work(self, input_items, output_items):
        output_items[0][0] = 3 * input_items[0][0]
        return 1


class Blk_source_output_arb_num(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Source: the number 213', in_sig=[], out_sig=[np.float32])
        self.i = 0

    def work(self, input_items, output_items):
        output_items[0][0] = self.i
        output_items[0][1] = self.i + 1
        output_items[0][2] = self.i + 2
        self.i += 3
        return 3

class Blk_arb_num_multiplied_by_three(gr.hier_block2):
    def __init__(self):
        """
        our configured hier block

        """
        gr.hier_block2.__init__(self, "arb_num_mult_three",
                                # Input signature
                                [],
                                [np.float32])      # Output signature

        self.connect(self, self.something, self.somethingelse, self)