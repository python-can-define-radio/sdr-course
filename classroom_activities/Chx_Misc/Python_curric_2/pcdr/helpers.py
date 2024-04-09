import numpy as np
from queue import SimpleQueue, Empty, Queue
from typing import List, TypeVar, Union, Optional, Type, overload
from typeguard import typechecked
from gnuradio import gr
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.types_and_contracts import HasWorkFunc
import attrs
from attrs import field, validators
import osmosdr



T = TypeVar('T')




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
    device_args: documented here: https://osmocom.org/projects/gr-osmosdr/wiki
    Others are documented on the Hack RF FAQ.
    """
    center_freq: float = field()
    @center_freq.validator
    def check(self, attribute, value):
        if not (1e6 <= value <= 6e9):
            raise ValueError(HACKRF_ERRORS.CENTER_FREQ)

    device_args: str = field(default="hackrf=0")

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
    device_args: documented here: https://osmocom.org/projects/gr-osmosdr/wiki
    Others are documented on the Hack RF FAQ.
    """
    center_freq: float = field()
    @center_freq.validator
    def check(self, attribute, value):
        if not (1e6 <= value <= 6e9):
            raise ValueError(HACKRF_ERRORS.CENTER_FREQ)

    device_args: str = field(default="hackrf=0")

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



@typechecked
def bytes_to_bin_list(b: Union[bytes, List[int]]) -> List[int]:
    """
    Converts each item in b to bits.

    Examples:
    
    >>> bytes_to_bin_list(b"C")
    [0, 1, 0, 0, 0, 0, 1, 1]

    >>> bytes_to_bin_list([67])
    [0, 1, 0, 0, 0, 0, 1, 1]

    >>> bytes_to_bin_list([192])
    [1, 1, 0, 0, 0, 0, 0, 0]

    >>> bytes_to_bin_list(b"CB")
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    """
    assert all(0 <= item < 256 for item in b)
    bitstrs = [f"{c:08b}" for c in b]
    joined = "".join(bitstrs)
    result = list(map(int, joined))
    assert len(result) == len(b) * 8
    assert all(x in [0, 1] for x in result)
    return result


NON_ASCII_ERR = "Currently, this only works for characters whose `ord` value is less than 256. For now, use `bytes_to_bin_list` if you wish to use non-ASCII characters. However, this may cause unexpected results for certain characters such as '«' that have multiple possible encodings."


@typechecked
def str_to_bin_list(message: str) -> List[int]:
    """
    Converts a string to a list of bits.

    Examples:

    >>> str_to_bin_list("C")
    [0, 1, 0, 0, 0, 0, 1, 1]

    >>> str_to_bin_list("CB")
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]

    >>> str_to_bin_list("«")
    [1, 0, 1, 0, 1, 0, 1, 1]
    """
    numeric = [ord(c) for c in message]
    if any(map(lambda x: x > 256, numeric)):
        raise ValueError(NON_ASCII_ERR)
    return bytes_to_bin_list(numeric)


@typechecked
def int_to_bin_list(message: np.ndarray) -> List[int]:
    """
    Converts a numpy array of integers to a list of bits. Capable handling of a variety of dtypes.

    Examples:

    >>> int_to_bin_list(np.array([0x43],dtype='uint8'))
    [0, 1, 0, 0, 0, 0, 1, 1]
    
    >>> int_to_bin_list(np.array([0x43,0x42],dtype='uint8'))
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    
    >>> int_to_bin_list(np.array([0x4342],dtype='uint16'))
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
	"""

    if ((message.dtype == 'int8')|(message.dtype == 'uint8')):
        bitlength = 8
    elif (((message.dtype == 'int16')|(message.dtype == 'uint16'))):
        bitlength = 16
    elif (((message.dtype == 'int32')|(message.dtype == 'uint32'))):
        bitlength = 32
    elif (((message.dtype == 'int64')|(message.dtype == 'uint64'))):
        bitlength = 64
    else:
        raise ValueError("Unsupported dtype")

    ret = [0]*bitlength*len(message)
    bitlist_index = 0
    shift_list = list(reversed(range(0,bitlength)))
    for x in message:
        for bit_index in shift_list:
            if x&(1<<bit_index) > 0:
                ret[bitlist_index] = 1
            bitlist_index = bitlist_index + 1
    return ret


def prepend_zeros_(data: np.ndarray, zeroCount: int):
    prepended = np.concatenate([np.zeros(zeroCount, dtype=data.dtype), data])
    assert isinstance(prepended, np.ndarray)
    assert prepended.dtype == data.dtype
    assert (prepended[zeroCount:] == data).all()
    return prepended


class DeviceParameterError(ValueError):
    pass


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
    from pcdr.our_GR_blocks import Blk_VecSingleItemStack

    probe = Blk_VecSingleItemStack(type_, vecsize)
    tb.connect(src_blk, probe)
    return probe

