from queue import SimpleQueue, Empty, Queue
import signal
import sys
from typing import Union, Type, overload

import attrs
from attrs import field, validators
from gnuradio import gr
import numpy as np
import osmosdr
from typeguard import typechecked



class DeviceParameterError(ValueError):
    pass


class HACKRF_ERRORS:
    """Just an organizational structure. Not intended for instantiation or mutation."""

    SAMP_RATE = ("The HackRF One is only capable of sample rates "
            "between 2 Million samples per second (2e6) and "
            "20 Million samples per second (20e6). "
            f"Your specified sample rate was outside of this range.")
    CENTER_FREQ = ("The HackRF One is only capable of center frequencies "
            "between 1 MHz (1e6) and 6 GHz (6e9). "
            f"Your specified frequency was outside of this range.")
    RX_IF_GAIN = ("The HackRF One, when in receive mode, is only capable "
            "of the following IF gain settings: "
            "[0, 8, 16, 24, 32, 40]. "
            f"Your specified IF gain was not one of these options.")
    RX_BB_GAIN = ("The HackRF One, when in receive mode, is only capable "
            "of the following BB gain settings: "
            "[0, 2, 4, 6, ..., 56, 58, 60, 62]. "
            f"Your specified BB gain was not one of these options.")
    TX_IF_GAIN = ("The HackRF One, when in transmit mode, is only capable "
            "of the following if gain settings: "
            "[0, 1, 2, 3, ..., 45, 46, 47]. "
            f"Your specified if gain was not one of these options.")


@attrs.define
class HackRFArgs_RX:
    """
    Used in GNU Radio's Osmocom Source block.
    
    Parameters
    ----------
    device_args :
        This is typically "hackrf=0" when using the Hack RF.  
        Options documented here: https://osmocom.org/projects/gr-osmosdr/wiki
    
    All others: 
        Documented on the Hack RF FAQ.
    """
    center_freq: float = field()
    @center_freq.validator
    def check(self, attribute, value):
        if not (1e6 <= value <= 6e9):
            raise ValueError(HACKRF_ERRORS.CENTER_FREQ)

    device_args: str = field()

    samp_rate: float = field(default=2e6)
    @samp_rate.validator
    def check(self, attribute, value):
        if not (2e6 <= value <= 20e6):
            raise ValueError(HACKRF_ERRORS.SAMP_RATE)

    rf_gain: int = field(default=0, validator=validators.ge(0))

    if_gain: int = field(default=24)
    @if_gain.validator
    def check(self, attribute, value):
        if value not in range(0, 40+8, 8):
            raise ValueError(HACKRF_ERRORS.RX_IF_GAIN)
        
    bb_gain: int = field(default=30)
    @bb_gain.validator
    def check(self, attribute, value):
        if value not in range(0, 62+2, 2):
            raise ValueError(HACKRF_ERRORS.RX_BB_GAIN)
        
    bandwidth: float = field(default=0)
    

@attrs.define
class HackRFArgs_TX:
    """
    Used in GNU Radio's Osmocom Sink block.
    
    Parameters
    ----------
    device_args :
        This is typically "hackrf=0" when using the Hack RF.  
        Options documented here: https://osmocom.org/projects/gr-osmosdr/wiki
    
    All others: 
        Documented on the Hack RF FAQ.
    """
    center_freq: float = field()
    @center_freq.validator
    def check(self, attribute, value):
        if not (1e6 <= value <= 6e9):
            raise ValueError(HACKRF_ERRORS.CENTER_FREQ)

    device_args: str = field()

    samp_rate: float = field(default=2e6)
    @samp_rate.validator
    def check(self, attribute, value):
        if not (2e6 <= value <= 20e6):
            raise ValueError(HACKRF_ERRORS.SAMP_RATE)

    rf_gain: int = field(default=0, validator=validators.ge(0))

    if_gain: int = field(default=24)
    @if_gain.validator
    def check(self, attribute, value):
        if value not in range(0, 47+1):
            raise ValueError(HACKRF_ERRORS.TX_IF_GAIN)
        
    bb_gain: int = field(default=30)
    @bb_gain.validator
    def check(self, attribute, value):
        if value not in range(0, 62+2, 2):
            raise ValueError(HACKRF_ERRORS.RX_BB_GAIN)
        
    bandwidth: float = field(default=0)


class CenterFrequencySettable:
    @typechecked
    def set_center_freq(self, center_freq: float) -> float:
        ## TODO: how to statically check that osmo has correct type?
        self._osmoargs.center_freq = center_freq
        return self._osmo.set_center_freq(center_freq)


class LockUnlockable:
    def lock(self):
        self._tb.lock()

    def unlock(self):
        self._tb.unlock()


class Startable:
    def start(self):
        self._tb.start()


class StopAndWaitable:
    def stop_and_wait(self):
        self._tb.stop()
        self._tb.wait()


class Waitable:
    def wait(self):
        self._tb.wait()


class IFGainSettable:
    @typechecked
    def set_if_gain(self, if_gain: float) -> float:
        self._osmoargs.if_gain = if_gain
        return self._osmo.set_if_gain(if_gain)


class BBGainSettable:
    @typechecked
    def set_bb_gain(self, bb_gain: float) -> float:
        self._osmoargs.bb_gain = bb_gain
        return self._osmo.set_bb_gain(bb_gain)


class ProbeReadable:
    @typechecked
    def read_probe(self) -> np.ndarray:
        if self._probe == None:
            raise AttributeError("The probe must be set using connect_probe().")
        return self._probe.sis._reading.get()


## Eventually, I imagine adding other devices, like
##  OsmocomArgs_RX = Union[HackRFArgs_RX, RTLSDRArgs_RX, ...]
OsmocomArgs_RX = HackRFArgs_RX
OsmocomArgs_TX = HackRFArgs_TX


@typechecked
def get_OsmocomArgs_RX(center_freq: float, device_args: str) -> OsmocomArgs_RX:
    if device_args.startswith("hackrf="):
        return HackRFArgs_RX(center_freq, device_args)
    else:
        raise NotImplementedError("In the current implementation, device_args must "
                                  "start with 'hackrf=', for example, 'hackrf=0'.")


@typechecked
def get_OsmocomArgs_TX(center_freq: float, device_args: str) -> OsmocomArgs_TX:
    if device_args.startswith("hackrf="):
        return HackRFArgs_TX(center_freq, device_args)
    else:
        raise NotImplementedError("In the current implementation, device_args must "
                                  "start with 'hackrf=', for example, 'hackrf=0'.")


@overload
def configureOsmocom(osmo_init_func: Type[osmosdr.source],
                     osmoargs: OsmocomArgs_RX
                     ) -> osmosdr.source: ...
@overload
def configureOsmocom(osmo_init_func: Type[osmosdr.sink],
                     osmoargs: OsmocomArgs_TX
                     ) -> osmosdr.sink: ...
@typechecked
def configureOsmocom(osmo_init_func,
                     osmoargs: Union[OsmocomArgs_RX, OsmocomArgs_TX]
                     ) -> Union[osmosdr.source, osmosdr.sink]:
    """
    Boilerplate for initializing an osmocom source or sink
    """
    ## TODO: The osmo_init_func is actually either osmosdr.source or osmosdr.sink,
    ## but since in this version of GNU Radio we can't specify that, these
    ## won't show correctly.
    osmo = osmo_init_func(osmoargs.device_args)
    osmo.set_center_freq(osmoargs.center_freq)
    osmo.set_sample_rate(osmoargs.samp_rate)
    osmo.set_gain(osmoargs.rf_gain)
    osmo.set_if_gain(osmoargs.if_gain)
    osmo.set_bb_gain(osmoargs.bb_gain)
    osmo.set_bandwidth(osmoargs.bandwidth)
    return osmo
    

def configure_graceful_exit(tb: gr.top_block):
    """The portion of GNU Radio boilerplate that 
    catches SIGINT and SIGTERM, and tells the flowgraph
    to gracefully stop before exiting the program.
    
    Used mainly for non-graphical flowgraphs."""
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)


@typechecked
def create_top_block_and_configure_exit() -> gr.top_block:
    tb = gr.top_block()
    configure_graceful_exit(tb)
    return tb


class QueueTypeWrapped(Queue):
    """
    Right now, this is actually just an alias for Queue.
    Someday, we may implement it similarly to `SimpleQueueTypeWrapped`.
    """
    pass


class SimpleQueueTypeWrapped(SimpleQueue):
    """For queues of numpy arrays of fixed length and type.
    
    The `dtype` parameter is the dtype of the numpy array contents.
    The `chunk_size` parameter is the length of each queue element.

    Example:
    >>> import numpy as np
    >>> q = SimpleQueueTypeWrapped(np.ndarray, np.complex64, 3)
    
    Normal usage:
    >>> q.put(np.array([10, 20, 30], dtype=np.complex64))
    >>> q.get()
    array([10.+0.j, 20.+0.j, 30.+0.j], dtype=complex64)
    
    Wrong type:
    >>> q.put(np.array([10, 20, 30]))
    Traceback (most recent call last):
      ...
    AssertionError...

    Wrong size:
    >>> q.put(np.array([10, 20], dtype=np.complex64))
    Traceback (most recent call last):
      ...
    AssertionError...
    """
    def __init__(self, qtype, dtype, chunk_size: int):
        if qtype != np.ndarray:
            raise NotImplementedError()
        self.qtype = qtype
        self.dtype = dtype
        self.chunk_size = chunk_size
        super().__init__()
    
    def put(self, item):
        assert isinstance(item, self.qtype)
        assert item.dtype == self.dtype
        assert len(item) == self.chunk_size
        return super().put(item)


@typechecked
def queue_to_list(q: SimpleQueue) -> list:
    """Converts a queue to a list.

    Note that this consumes the queue, so running a second time on
    a queue without changing the queue will produce an empty list.
    
    Examples:
    >>> from queue import SimpleQueue
    
    >>> q = SimpleQueue()
    >>> q.put(3)
    >>> q.put(5)
    
    Normal usage:
    >>> queue_to_list(q)
    [3, 5]

    Running a second time on the same queue:
    >>> queue_to_list(q)
    []

    Putting more data into the queue:
    >>> q.put(6)
    >>> queue_to_list(q)
    [6]

    A trivial example of an empty queue (just for doctest):
    >>> q = SimpleQueue()
    >>> queue_to_list(q)
    []
    """
    ## Unfortunately I have to remove the "better"
    ## type annotations for now, such as SimpleQueue[T]
    retval = []
    while True:
        try:
            retval.append(q.get_nowait())
        except Empty:
            return retval


def prepend_zeros_(data: np.ndarray, zeroCount: int):
    prepended = np.concatenate([np.zeros(zeroCount, dtype=data.dtype), data])
    assert isinstance(prepended, np.ndarray)
    assert prepended.dtype == data.dtype
    assert (prepended[zeroCount:] == data).all()
    return prepended



@typechecked
def validate_hack_rf_transmit(device_name: str,
                              samp_rate: float,
                              center_freq: float,
                              if_gain: int):
    if device_name != "hackrf":
        return
    
    if not (2e6 <= samp_rate <= 20e6):
        raise DeviceParameterError(
            "The HackRF One is only capable of sample rates "
            "between 2 Million samples per second (2e6) and "
            "20 Million samples per second (20e6). "
            f"Your specified sample rate, {samp_rate}, was outside of this range."
        )
    
    if not (1e6 < center_freq < 6e9):
        raise DeviceParameterError(
            "The HackRF One is only capable of center frequencies "
            "between 1 MHz (1e6) and 6 GHz (6e9). "
            f"Your specified frequency, {center_freq}, was outside of this range."
        )
    
    if not if_gain in range(0, 47+1, 1):
        raise DeviceParameterError(
            "The HackRF One, when in transmit mode, is only capable "
            "of the following IF gain settings: "
            "[0, 1, 2, ... 45, 46, 47]. "
            f"Your specified IF gain, {if_gain}, was not one of these options."
        )
    

@typechecked
def getSize(dtype: type) -> int:
    if dtype == np.complex64:
        return gr.sizeof_gr_complex
    elif dtype == np.float32:
        return gr.sizeof_float
    elif dtype == np.int32:
        return gr.sizeof_int
    elif dtype == np.int16:
        return gr.sizeof_short
    elif dtype == np.uint8:
        return gr.sizeof_char
    else:
        return NotImplementedError("Feel free to add more dtype matches")


@typechecked
def connect_probe_common(tb: gr.top_block, src_blk, type_: type, vecsize: int):
    ## placed here to avoid circular imports
    from pcdr._internal.our_GR_blocks import Blk_VecSingleItemStack

    probe = Blk_VecSingleItemStack(type_, vecsize)
    tb.connect(src_blk, probe)
    return probe


def gnuradio_send(data: np.ndarray,
                  center_freq: float,
                  samp_rate: float,
                  if_gain: int = 16,
                  device_args: str = "hackrf=0",
                  repeat: bool = False):
    """Sends `data` to osmocom sink."""
    from pcdr._internal.vector_tx_flowgraphs import vector_to_osmocom_sink
    normal_py_data = list(map(complex, data))  # GNURadio type issues. Eventually, fix this for efficiency
    tb = vector_to_osmocom_sink(normal_py_data, center_freq, samp_rate, if_gain, device_args, repeat)
    configure_graceful_exit(tb)
    tb.start()
    tb.wait()
