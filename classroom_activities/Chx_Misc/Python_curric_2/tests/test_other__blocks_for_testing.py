from typing import List
from io import StringIO
import time
from unittest.mock import patch
from gnuradio import gr, analog
import numpy as np
from typeguard import typechecked
from pcdr._internal.our_GR_blocks import Blk_sink_print
from pcdr._internal.basictermplot import plot



class Blk_mult_three(gr.sync_block):
    @typechecked
    def __init__(self, in_sig: List[type], out_sig: List[type]):
        """in_sig used to be [np.uint8];
        out_sig used to be [np.float32]"""
        gr.sync_block.__init__(self, 'Multiply by three', in_sig, out_sig)

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
        A simple hier block that outputs 0, 3, 6, ...; largely for a model for others.
        """
        gr.hier_block2.__init__(
            self, 
            "arb num, mult by three",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_float)
        )

        self.arb = Blk_source_output_arb_num()
        self.mul3 = Blk_mult_three([np.float32], [np.float32])
        self.connect(self.arb, self.mul3, self)


class Blk_fake_osmosdr_source(gr.hier_block2):
    @typechecked
    def __init__(self, fake_samp_rate: float, fake_center_freq: float):
        """Return a block that resembles the osmosdr_source, but always has activity at only 200kHz."""
        
        gr.hier_block2.__init__(
            self, 
            "Fake osmocom source",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_gr_complex)
        )

        self.fake_samp_rate = fake_samp_rate
        self.fake_center_freq = fake_center_freq
        fake_activity_freq = 200e3
        
        self.analog_sig_source = analog.sig_source_c(
            fake_samp_rate, analog.GR_COS_WAVE, 
            fake_activity_freq - fake_center_freq, 1)
        
        self.connect(self.analog_sig_source, self)

    @typechecked
    def set_sample_rate(self, samp_rate: float):
        assert self.fake_samp_rate == samp_rate

    @typechecked
    def set_center_freq(self, center_freq: float):
        assert self.fake_center_freq == center_freq
        
    @typechecked
    def set_gain(self, g: float):
        pass

    @typechecked
    def set_if_gain(self, g: float):
        pass

    @typechecked
    def set_bb_gain(self, g: float):
        pass


@patch('sys.stdout', new_callable=StringIO)
def test_Blk_source_output_arb_num(output: StringIO):
    tb = gr.top_block()
    arb = Blk_source_output_arb_num()
    pri = Blk_sink_print()
    tb.connect(arb, pri)
    tb.start()
    time.sleep(0.3)
    tb.stop()
    tb.wait()
    outv = output.getvalue()
    assert len(outv) > 0
    spl = outv.split("\n")
    assert len(spl) > 0
    assert spl[:4] == [
        '0.0', '1.0', '2.0', '3.0'
    ]
    

@patch('sys.stdout', new_callable=StringIO)
def test_Blk_arb_num_multiplied_by_three(output: StringIO):
    tb = gr.top_block()
    arb3 = Blk_arb_num_multiplied_by_three()
    pri = Blk_sink_print()
    tb.connect(arb3, pri)
    tb.start()
    time.sleep(0.3)
    tb.stop()
    tb.wait()
    outv = output.getvalue()
    assert len(outv) > 0
    spl = outv.split("\n")
    assert len(spl) > 0
    assert spl[:4] == [
        '0.0', '3.0', '6.0', '9.0'
    ]


@patch('sys.stdout', new_callable=StringIO)
def test_Blk_fake_osmosdr_source(output: StringIO):
    fake_center_freq = 170e3
    tb = gr.top_block()
    osm = Blk_fake_osmosdr_source(2e6, fake_center_freq)
    pri = Blk_sink_print(dtype=np.complex64)
    tb.connect(osm, pri)
    tb.start()
    time.sleep(0.3)
    tb.stop()
    tb.wait()
    outv = output.getvalue()
    assert len(outv) > 0
    spl = outv.split("\n")
    assert len(spl) > 0
    parsed = np.array(list(map(complex, spl[:50])))
    plotOutput = StringIO()
    plot(np.array(range(len(parsed))), parsed.real, output_stream=plotOutput)
    ## TODO: I haven't verified that the wave has the right frequency.
    assert plotOutput.getvalue() == """\
xmin: 0.00
xmax: 49.00
ymin: -1.00
ymax: 1.00
~o█████████████████████████████████████████████████
~█oooooooo█████████████████████████████████████████
~█████████ooo██████████████████████████████████████
~████████████oooo██████████████████████████████████
~████████████████ooo██████████████████████████████o
~███████████████████ooo████████████████████████ooo█
~██████████████████████oooo████████████████oooo████
~██████████████████████████oooooooooooooooo████████
"""
