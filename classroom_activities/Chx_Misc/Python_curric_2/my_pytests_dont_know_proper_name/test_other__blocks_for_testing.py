from gnuradio import gr


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
