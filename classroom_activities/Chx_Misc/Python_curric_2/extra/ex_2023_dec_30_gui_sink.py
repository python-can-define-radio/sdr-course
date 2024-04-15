from pcdr._beta.gnuradio_sendlike import _configure_and_run_gui_flowgraph
from pcdr._internal.queue_to_guisink_flowgraph import queue_to_guisink
from pcdr._internal.misc import SimpleQueueTypeWrapped
import numpy as np

if __name__ == "__main__":
    chunk_size = 2**20
    q = SimpleQueueTypeWrapped(np.ndarray, np.complex64, chunk_size)
    q.put(np.linspace(0, 100, chunk_size, dtype=np.complex64))
    _configure_and_run_gui_flowgraph(queue_to_guisink, [104.3e6, 2e6, q, chunk_size])
