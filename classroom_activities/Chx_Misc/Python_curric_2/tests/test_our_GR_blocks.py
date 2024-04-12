from gnuradio import gr, analog, blocks
from pcdr._internal.our_GR_blocks import Blk_strength_at_freq, SingleItemStack, Averager
import time
import pytest
import queue




def test_Blk_strength_at_freq_1():
    samp_rate = 10_000
    fft_size = 1024
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                1000, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, fft_size)
    saf = Blk_strength_at_freq(samp_rate, 1000, fft_size)
    
    tb.connect(sig_s, stream_to_vec, saf)
    tb.start()
    assert saf._reading.get() > 650
    tb.stop()
    tb.wait()


def test_Blk_strength_at_freq_2():
    samp_rate = 10_000
    fft_size = 1024
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                3000, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, fft_size)
    saf = Blk_strength_at_freq(samp_rate, 1000, fft_size)
    
    tb.connect(sig_s, stream_to_vec, saf)
    tb.start()
    assert saf._reading.get() < 6
    tb.stop()
    tb.wait()


def test_Blk_strength_at_freq_3():
    samp_rate = 10_000
    fft_size = 1024
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                4800, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, fft_size)
    saf = Blk_strength_at_freq(samp_rate, 4800, fft_size)
    
    tb.connect(sig_s, stream_to_vec, saf)
    tb.start()
    assert saf._reading.get() > 650
    tb.stop()
    tb.wait()


def test_Blk_strength_at_freq_4():
    samp_rate = 10_000
    fft_size = 1024
    tb = gr.top_block()
    sig_s = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE,
                                3000, 1)
    stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, fft_size)
    saf = Blk_strength_at_freq(samp_rate, 4800, fft_size)
    
    tb.connect(sig_s, stream_to_vec, saf)
    tb.start()
    assert saf._reading.get() < 6
    tb.stop()
    tb.wait()


def test_SingleItemStack_can_add_one():
    s = SingleItemStack()
    s.put(42)
    assert s.get() == 42


def test_SingleItemStack_can_add_two():
    """Notice that the first item that was `put()` is gone."""
    s = SingleItemStack()
    s.put(42)
    s.put(43)
    assert s.get() == 43
    with pytest.raises(queue.Empty):
        s.get(timeout=0.01)


def test_Averager():
    a = Averager()
    assert "Something that is useful in Blk_strength_at_freq"
