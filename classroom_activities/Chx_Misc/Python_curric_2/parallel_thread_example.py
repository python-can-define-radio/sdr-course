import time


def parallel_thread(tb):
    while True:
        tb.osmocom.set_center_freq(104.3e6)
        time.sleep(1)
        tb.osmocom.set_center_freq(93.9e6)
        time.sleep(1)


start_gui_and_run_thread(noise_jammer, parallel_thread)
