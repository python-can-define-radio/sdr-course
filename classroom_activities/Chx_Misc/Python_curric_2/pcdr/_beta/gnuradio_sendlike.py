from distutils.version import StrictVersion
from queue import Empty
import signal
import sys
from typing import List, Optional, Sequence, TypeVar, Union

import numpy as np
from gnuradio import gr

from pcdr._beta.osmocom_queued_tx_flowgraph import queue_to_osmocom_sink, queue_to_print_sink, queue_to_string_file_sink, queue_to_file_sink, queue_to_zmqpub_sink
from pcdr._internal.misc import SimpleQueueTypeWrapped, queue_to_list, prepend_zeros_, configure_graceful_exit
from pcdr._internal.vector_tx_flowgraphs import vector_to_file_sink, vector_to_osmocom_sink
from pcdr._internal.types_and_contracts import TRealNum, TRealOrComplexNum
from pcdr._internal.queue_to_guisink_flowgraph import queue_to_guisink
from pcdr._internal.vector_to_guisink_flowgraph import vector_to_guisink



try:
    ## Why this import is here:
    ## We don't want Qt to be required for ALL pcdr uses;
    ## just graphical ones.
    from PyQt5 import Qt


    def _configure_and_run_gui_flowgraph(top_block_cls, args):
        """The portion of GNU Radio boilerplate that 
        sets up the QT GUI Application."""
        if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        qapp = Qt.QApplication(sys.argv)

        tb = top_block_cls(*args)
        tb.start()
        tb.show()

        def sig_handler(sig=None, frame=None):
            Qt.QApplication.quit()

        signal.signal(signal.SIGINT, sig_handler)
        signal.signal(signal.SIGTERM, sig_handler)

        timer = Qt.QTimer()
        timer.start(500)
        timer.timeout.connect(lambda: None)

        def quitting():
            tb.stop()
            tb.wait()
        qapp.aboutToQuit.connect(quitting)
        qapp.exec_()

except ModuleNotFoundError:
    pass


def _pad_chunk_queue(data: np.ndarray, chunk_size: int) -> SimpleQueueTypeWrapped:
    """
    - numpy-ify
    - Pad `data` to a multiple of `chunk_size`
    - Split into chunks of that size
    - Convert to a queue of numpy arrays for gnuradio use
    
    Examples:
    >>> testdata = np.array([1, 2, 3], dtype=np.uint8)
    >>> pcq = _pad_chunk_queue(testdata, 2)
    >>> pcq.get()
    array([1.+0.j, 2.+0.j], dtype=complex64)
    >>> pcq.get()
    array([3.+0.j, 0.+0.j], dtype=complex64)

    >>> testdata = np.array([1, 2, 3], dtype=np.uint8)
    >>> pcq = _pad_chunk_queue(testdata, 5)
    >>> nparry = np.array(queue_to_list(pcq))
    >>> should_be = np.array([[1, 2, 3, 0, 0]], dtype=np.complex64)
    >>> assert (nparry == should_be).all()
    """
    assert 0 < chunk_size
    assert len(data.shape) == 1  # Require 1-dimensional array (`shape` has only one item, that is, one dimension)
    npdata = np.array(data, dtype=np.complex64)
    assert type(npdata) == np.ndarray
    assert npdata.dtype == np.complex64
    assert len(npdata.shape) == 1
    
    ## Pad to next full chunk size, then chunk
    padlen = chunk_size - (len(npdata) % chunk_size)
    if padlen != chunk_size:
        npdata = np.concatenate([npdata, np.zeros(padlen, dtype=np.complex64)])
    assert len(npdata) % chunk_size == 0
    chunked = np.split(npdata, len(npdata)/chunk_size)

    q = SimpleQueueTypeWrapped(np.ndarray, np.complex64, chunk_size)
    for item in chunked:
        q.put(item)
    assert issubclass(q.qtype, np.ndarray)
    return q


def _gnuradio_guisink_using_queue_impl(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  prepend_zeros: int = 0,
                  chunk_size: int = 1024):
    """Display using a GNU Radio QT GUI Sink."""
    prepended = np.concatenate([np.zeros(prepend_zeros, dtype=data.dtype), data])
    assert prepended.dtype == data.dtype
    assert (prepended[prepend_zeros:] == data).all()
    q = _pad_chunk_queue(prepended, chunk_size)

    _configure_and_run_gui_flowgraph(queue_to_guisink, [center_freq, samp_rate, q, chunk_size])


def gnuradio_guisink(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  prepend_zeros: int = 0):
    """Display using a GNU Radio QT GUI Sink."""
    prepended = prepend_zeros_(data, prepend_zeros)
    normal_py_data = tuple(map(complex, prepended))  # GNURadio type issues. Eventually, fix this for efficiency
    _configure_and_run_gui_flowgraph(vector_to_guisink, [center_freq, samp_rate, normal_py_data])


def _gnuradio_print_using_queue_impl(data: np.ndarray, print_delay: float = 0.5, chunk_size: int = 1024):
    """Sends data to a print block."""
    q = _pad_chunk_queue(data, chunk_size)
    tb = queue_to_print_sink(print_delay, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


# def gnuradio_print():
#     raise NotImplementedError()


# def gnuradio_write_text_file():
#     raise NotImplementedError()


def _gnuradio_write_text_file_using_queue_impl(data: np.ndarray, filename: str, chunk_size: int = 1024):
    """Writes data to a file named `filename`, encoded as text.
    NOTE: Based on issues experienced with _gnuradio_write_file, this may not write the entire file."""
    q = _pad_chunk_queue(data, chunk_size)
    tb = queue_to_string_file_sink(filename, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def _gnuradio_write_file_using_queue_impl(data: np.ndarray, filename: str, chunk_size: int = 1024):
    """Writes data to a file named `filename`, encoded as np.complex64.
    NOTE: There seem to be unresolved issues in which this does not write a full file."""
    q = _pad_chunk_queue(data, chunk_size)
    tb = queue_to_file_sink(filename, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def _gnuradio_write_file(data: np.ndarray, filename: str):
    """Writes data to a file named `filename`, encoded as np.complex64.
    NOTE: There seem to be an unresolved issue in which this does not write a full file."""
    normal_py_data = tuple(map(complex, data))  # GNURadio type issues. Eventually, fix this for efficiency
    tb = vector_to_file_sink(normal_py_data, filename)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def _gnuradio_network_pub(data: np.ndarray, port: int = 8008, chunk_size: int = 1024):
    """NOT FULLY TESTED. 
    Use a TCP socket to transmit data to a host on the network (also works for localhost).
    (Note: implemented using ZeroMQ.)"""
    q = _pad_chunk_queue(data, chunk_size)
    tb = queue_to_zmqpub_sink(port, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def _gnuradio_send_using_queue_impl(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  if_gain: int = 16,
                  device_args: str = "hackrf=0",
                  chunk_size: int = 1024):
    """Sends `data` to osmocom sink."""
    q = _pad_chunk_queue(data, chunk_size)
    tb = queue_to_osmocom_sink(center_freq, samp_rate, chunk_size, if_gain, q, device_args)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()
