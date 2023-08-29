from typing import List, Optional, Sequence, TypeVar, Union
import deal
import pydash
import numpy as np
from queue import Empty
from pcdr.helpers import SimpleQueueTypeWrapped, queue_to_list
from pcdr.osmocom_queued_tx_flowgraph import queue_to_osmocom_sink, queue_to_print_blk, queue_to_string_file_sink, queue_to_file_sink
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.types_and_contracts import TRealNum, TRealOrComplexNum
from pcdr.osmocom_queued_tx_flowgraph import queue_to_zmqpub_sink
from pcdr.queue_to_guisink_flowgraph import queue_to_guisink
from pcdr.gnuradio_misc import configure_and_run_gui_flowgraph


T = TypeVar('T')


def __pad_chunk_queue_test_1():
    testdata = np.array([1, 2, 3], dtype=np.uint8)
    pcq = pad_chunk_queue(testdata, 2)
    nparry = np.array(queue_to_list(pcq))
    should_be = np.array([[1, 2], [3, 0]], dtype=np.complex64)
    return (nparry == should_be).all()


def __pad_chunk_queue_test_2():
    testdata = np.array([1, 2, 3], dtype=np.uint8)
    pcq = pad_chunk_queue(testdata, 5)
    nparry = np.array(queue_to_list(pcq))
    should_be = np.array([[1, 2, 3, 0, 0]], dtype=np.complex64)
    return (nparry == should_be).all()
    


@deal.example(__pad_chunk_queue_test_1)
@deal.example(__pad_chunk_queue_test_2)
@deal.ensure(lambda _:  \
        queue_to_list(_.result) == [] if len(_.data) == 0 else True,
        message="If data is empty, then the result is an empty queue"
)
@deal.pre(lambda _: 0 < _.chunk_size < int(50e6))
@deal.pre(lambda _: np.isfinite(_.data).all())
# Require 1-dimensional array (`shape` has only one item, that is, one dimension)
@deal.pre(lambda _: len(_.data.shape) == 1)
@deal.post(lambda result: issubclass(result.qtype, np.ndarray))
@deal.has()
def pad_chunk_queue(data: np.ndarray, chunk_size: int) -> SimpleQueueTypeWrapped:
    """
    - numpy-ify
    - Pad `data` to a multiple of `chunk_size`
    - Split into chunks of that size
    - Convert to a queue of numpy arrays for gnuradio use"""

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
    return q


def gnuradio_guisink(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  prepend_zeros: int = 0,
                  chunk_size: int = 1024):
    """Display using a GNU Radio QT GUI Sink"""
    prepended = np.concatenate([np.zeros(prepend_zeros, dtype=data.dtype), data])
    assert prepended.dtype == data.dtype
    assert (prepended[prepend_zeros:] == data).all()
    q = pad_chunk_queue(prepended, chunk_size)

    configure_and_run_gui_flowgraph(queue_to_guisink, [center_freq, samp_rate, q, chunk_size])
    

def gnuradio_print(data: np.ndarray, print_delay: float = 0.5, chunk_size: int = 1024):
    """Sends data to a print block."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_print_blk(print_delay, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_write_text_file(data: np.ndarray, filename: str, chunk_size: int = 1024):
    """Writes data to a file named `filename`, encoded as text."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_string_file_sink(filename, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_write_file(data: np.ndarray, filename: str, chunk_size: int = 1024):
    """Writes data to a file named `filename`, encoded as np.complex64."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_file_sink(filename, q, chunk_size)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()


def gnuradio_network_pub(data: np.ndarray, port: int = 8008, chunk_size: int = 1024):
    """Use a TCP socket to transmit data to a host on the network (also works for localhost).
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
                  chunk_size: int = 1024):
    """Sends to osmocom sink."""
    q = pad_chunk_queue(data, chunk_size)
    tb = queue_to_osmocom_sink(center_freq, samp_rate, chunk_size, if_gain, q, device_args)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()
