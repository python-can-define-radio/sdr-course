from typing import List, Optional, Sequence, TypeVar, Union
import numpy as np
from queue import Empty
from pcdr.helpers import SimpleQueueTypeWrapped, queue_to_list, prepend_zeros_
from pcdr.osmocom_queued_tx_flowgraph import queue_to_osmocom_sink, queue_to_print_sink, queue_to_string_file_sink, queue_to_file_sink
from pcdr.vector_tx_flowgraphs import vector_to_file_sink, vector_to_osmocom_sink
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.types_and_contracts import TRealNum, TRealOrComplexNum
from pcdr.osmocom_queued_tx_flowgraph import queue_to_zmqpub_sink
from pcdr.queue_to_guisink_flowgraph import queue_to_guisink
from pcdr.vector_to_guisink_flowgraph import vector_to_guisink
from pcdr.gnuradio_misc import configure_and_run_gui_flowgraph


T = TypeVar('T')



def pad_chunk_queue(data: np.ndarray, chunk_size: int) -> SimpleQueueTypeWrapped:
    """
    - numpy-ify
    - Pad `data` to a multiple of `chunk_size`
    - Split into chunks of that size
    - Convert to a queue of numpy arrays for gnuradio use
    
    Examples:
    >>> testdata = np.array([1, 2, 3], dtype=np.uint8)
    >>> pcq = pad_chunk_queue(testdata, 2)
    >>> pcq.get()
    array([1.+0.j, 2.+0.j], dtype=complex64)
    >>> pcq.get()
    array([3.+0.j, 0.+0.j], dtype=complex64)

    >>> testdata = np.array([1, 2, 3], dtype=np.uint8)
    >>> pcq = pad_chunk_queue(testdata, 5)
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


def gnuradio_guisink_using_queue_impl(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  prepend_zeros: int = 0,
                  chunk_size: int = 1024):
    """Display using a GNU Radio QT GUI Sink."""
    prepended = np.concatenate([np.zeros(prepend_zeros, dtype=data.dtype), data])
    assert prepended.dtype == data.dtype
    assert (prepended[prepend_zeros:] == data).all()
    q = pad_chunk_queue(prepended, chunk_size)

    configure_and_run_gui_flowgraph(queue_to_guisink, [center_freq, samp_rate, q, chunk_size])


def gnuradio_guisink(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  prepend_zeros: int = 0):
    """Display using a GNU Radio QT GUI Sink."""
    prepended = prepend_zeros_(data, prepend_zeros)
    normal_py_data = tuple(map(complex, prepended))  # GNURadio type issues. Eventually, fix this for efficiency
    configure_and_run_gui_flowgraph(vector_to_guisink, [center_freq, samp_rate, normal_py_data])


def gnuradio_print_using_queue_impl(data: np.ndarray, print_delay: float = 0.5, chunk_size: int = 1024):
    """Sends data to a print block."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_print_sink(print_delay, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_print():
    raise NotImplementedError()


def gnuradio_write_text_file():
    raise NotImplementedError()


def gnuradio_write_text_file_using_queue_impl(data: np.ndarray, filename: str, chunk_size: int = 1024):
    """Writes data to a file named `filename`, encoded as text.
    NOTE: Based on issues experienced with gnuradio_write_file, this may not write the entire file."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_string_file_sink(filename, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_write_file_using_queue_impl(data: np.ndarray, filename: str, chunk_size: int = 1024):
    """Writes data to a file named `filename`, encoded as np.complex64.
    NOTE: There seem to be unresolved issues in which this does not write a full file."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_file_sink(filename, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_write_file(data: np.ndarray, filename: str):
    """Writes data to a file named `filename`, encoded as np.complex64.
    NOTE: There seem to be an unresolved issue in which this does not write a full file."""
    normal_py_data = tuple(map(complex, data))  # GNURadio type issues. Eventually, fix this for efficiency
    tb = vector_to_file_sink(normal_py_data, filename)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_network_pub(data: np.ndarray, port: int = 8008, chunk_size: int = 1024):
    """NOT FULLY TESTED. 
    Use a TCP socket to transmit data to a host on the network (also works for localhost).
    (Note: implemented using ZeroMQ.)"""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_zmqpub_sink(port, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_send(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  if_gain: int = 16,
                  device_args: str = "hackrf=0",
                  repeat: bool = False):
    """Sends `data` to osmocom sink."""
    normal_py_data = tuple(map(complex, data))  # GNURadio type issues. Eventually, fix this for efficiency
    tb = vector_to_osmocom_sink(normal_py_data, center_freq, samp_rate, if_gain, device_args, repeat)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_send_using_queue_impl(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  if_gain: int = 16,
                  device_args: str = "hackrf=0",
                  chunk_size: int = 1024):
    """Sends `data` to osmocom sink."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_osmocom_sink(center_freq, samp_rate, chunk_size, if_gain, q, device_args)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()
