import time

from qt_block_init import set_up_qt_top_block_and_run_func_in_thread

from basic_transmitter import basic_transmitter


def dostuff(tb):
    # type: (basic_transmitter) -> None
    
    while True:
        for offset in range(800):
            newFreq = 100e6 + offset*1e3
            tb.osmosdr_sink_0.set_center_freq(newFreq)
            time.sleep(0.01)


set_up_qt_top_block_and_run_func_in_thread(basic_transmitter, dostuff)


