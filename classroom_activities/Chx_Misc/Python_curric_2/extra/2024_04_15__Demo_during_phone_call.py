import time
from pcdr.flow import OsmosdrSingleFreqReceiver

def main():
    print("")
    print()
    while True:
        st = receiver.get_strength()
        if st > 20:
            print(f"Activity detected! Strength: {st}")
        time.sleep(0.01)

receiver = OsmosdrSingleFreqReceiver("hackrf=0", 463.2e6)
receiver.start_and_run_thread(main)

####################

# from pcdr import gnuradio_send, ook_modulate

# modulated = ook_modulate([1, 0, 1, 1, 0], int(1e6))
# gnuradio_send(modulated, 104.3e6, samp_rate=2e6)

######################
# import time
# from pcdr.flow import OsmoWindowReceiver

# ## Consider doing averaging over a time period

# averager = Averager(0)

# receiver = OsmoWindowReceiver()
# receiver.start()
# while True:
#     window = receiver.read_window()

#     st = window.avg_strength_between(462.3e6, 462.5e6)
#     if st > 20:
#         print(f"Activity detected on 462 band!")

#     st_465 = window.avg_strength_between(465.3e6, 465.5e6)
#     if st_465 > 20:
#         print(f"Activity detected on 465 band!")
        
#     time.sleep(0.01)


# receiver = OsmoWindowReceiver()
# receiver.start()
# while True:
#     window = receiver.read_window()

#     freqs = window.freqs_above_thresh(20)
#     if len(freqs) > 0:
#         beep()
#         print(f"Activity on {freqs}")
#     time.sleep(0.01)
