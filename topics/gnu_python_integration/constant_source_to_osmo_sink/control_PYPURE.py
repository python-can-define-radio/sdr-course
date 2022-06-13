import time

from qt_block_init_PYPURE import set_up_qt_top_block_and_run_func_in_thread

from basic_transmitter_GRCGEN import basic_transmitter_GRCGEN


def dostuff(tb):
    # type: (basic_transmitter_GRCGEN) -> None

    time.sleep(3)
    tb.osmosdr_sink_0.set_center_freq(101e6)
    
    time.sleep(3)
    tb.osmosdr_sink_0.set_center_freq(102e6)


set_up_qt_top_block_and_run_func_in_thread(basic_transmitter_GRCGEN, dostuff)


