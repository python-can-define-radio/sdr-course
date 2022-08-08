import numpy as np
import time

from qt_block_init_PURE import set_up_qt_top_block_and_run_func_in_thread

from zmq_socket_setup_PURE import makeZMQPushSocket

from zmq_pull_inversefft_GRCGEN import zmq_pull_inversefft_GRCGEN



def dostuff(tb):
    
    push_sock = makeZMQPushSocket("tcp://127.0.0.1:50252")
    
    samp_rate = 8e6  # samples per sec
    if tb.samp_rate != samp_rate:
        print("Sample rate should match but does not!\n"*10)

    
    while True:
        for fr in range(256, 768):
            tosend = np.zeros(1024, dtype=np.complex64)
            tosend[fr] = 1
            for unused in range(200):
                push_sock.send(tosend.tobytes())

    

set_up_qt_top_block_and_run_func_in_thread(zmq_pull_inversefft_GRCGEN, dostuff)