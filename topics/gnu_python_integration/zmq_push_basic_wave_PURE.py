import numpy as np

from qt_block_init_PURE import set_up_qt_top_block_and_run_func_in_thread

from zmq_socket_setup_PURE import makeZMQPushSocket

from zmq_pull_GRCGEN import zmq_pull_GRCGEN



def makewave(samp_rate, wave_freq_hz):

    one_cycle_len = samp_rate / wave_freq_hz  # samples

    # num_cycles_per_chunk should be an integer.
    # Too big will make each chunk of data too long, 
    # causing your RAM to max out.
    # Too small will make each chunk of data too short,
    # slowing down the flowgraph and possibly causing
    # the Hack RF to underflow.
    # My formula is intended to make it so chunk_len is about
    # 4096 (or larger as needed to ensure one full wave cycle
    #  is transmittted).
    num_cycles_per_chunk = max(1, int(4096 / one_cycle_len)) 

    chunk_len = one_cycle_len * num_cycles_per_chunk  # samples
    return np.exp(wave_freq_hz * 2 * 1j * np.pi * np.arange(chunk_len, dtype=np.complex64)/samp_rate)
    


def dostuff(tb):
    
    push_sock = makeZMQPushSocket("tcp://127.0.0.1:50252")
    
    samp_rate = 2e6  # samples per sec
    if tb.samp_rate != samp_rate:
        print("Sample rate should match but does not!\n"*10)

    somewave = makewave(samp_rate, 200e3)

    count = 0
    while True:
        
        for unused in range(500):
            push_sock.send(somewave.tobytes())

        for unused in range(10):
            zeros = np.zeros(100000, dtype=np.complex64)
            push_sock.send(zeros.tobytes())

        count += 1
        print("buffered:", count)
    

set_up_qt_top_block_and_run_func_in_thread(zmq_pull_GRCGEN, dostuff)