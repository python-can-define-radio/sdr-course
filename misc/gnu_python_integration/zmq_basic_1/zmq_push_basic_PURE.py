import numpy as np
import time

from qt_block_init_PURE import set_up_qt_top_block_and_run_func_in_thread

from zmq_socket_setup_PURE import makeZMQPushSocket

from zmq_pull_GRCGEN import zmq_pull_GRCGEN


def dostuff(tb):
    
    push_sock = makeZMQPushSocket("tcp://127.0.0.1:50252")
    
    ones = np.ones(100000, dtype=np.complex64)
    push_sock.send(ones.tobytes())
    

set_up_qt_top_block_and_run_func_in_thread(zmq_pull_GRCGEN, dostuff)