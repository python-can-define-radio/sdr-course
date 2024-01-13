from gnuradio import gr, analog, blocks
from pcdr.our_GR_blocks import Blk_strength_at_freq
import time


def test_Blk_strength_at_freq_1():
    samp_rate = 10_000
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                1000, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, 1024)
    saf = Blk_strength_at_freq(samp_rate, 1000)
    
    tb.connect(sig_s, stream_to_vec, saf)
    assert saf.latest_reading == 0
    tb.start()
    time.sleep(0.5)
    assert saf.latest_reading > 650
    tb.stop()
    tb.wait()


def test_Blk_strength_at_freq_2():
    samp_rate = 10_000
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                3000, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, 1024)
    saf = Blk_strength_at_freq(samp_rate, 1000)
    
    tb.connect(sig_s, stream_to_vec, saf)
    assert saf.latest_reading == 0
    tb.start()
    time.sleep(0.5)
    assert saf.latest_reading < 6
    tb.stop()
    tb.wait()


def test_Blk_strength_at_freq_3():
    samp_rate = 10_000
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                4800, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, 1024)
    saf = Blk_strength_at_freq(samp_rate, 4800)
    
    tb.connect(sig_s, stream_to_vec, saf)
    assert saf.latest_reading == 0
    tb.start()
    time.sleep(0.5)
    assert saf.latest_reading > 650
    tb.stop()
    tb.wait()


def test_Blk_strength_at_freq_4():
    samp_rate = 10_000
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                3000, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, 1024)
    saf = Blk_strength_at_freq(samp_rate, 4800)
    
    tb.connect(sig_s, stream_to_vec, saf)
    assert saf.latest_reading == 0
    tb.start()
    time.sleep(0.5)
    assert saf.latest_reading < 6
    tb.stop()
    tb.wait()


if __name__ == "__main__":
    test_Blk_strength_at_freq_1()