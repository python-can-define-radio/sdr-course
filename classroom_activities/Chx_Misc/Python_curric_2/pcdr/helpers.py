import numpy as np
from queue import SimpleQueue, Empty
from typing import List, TypeVar, Union, Optional



T = TypeVar('T')



class SimpleQueueTypeWrapped(SimpleQueue):
    """Created this as an alternative to SimpleQueue because Python 3.8 (which we're stuck with currently)
    doesn't support the type annotation SimpleQueue[something].

    This is specifically for queues of numpy arrays of fixed length and type.
    
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
    AssertionError

    Wrong size:
    >>> q.put(np.array([10, 20], dtype=np.complex64))
    Traceback (most recent call last):
      ...
    AssertionError
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


def validate_hack_rf_receive(device_args: str,
                             samp_rate: float,
                             center_freq: float,
                             if_gain: int,
                             bb_gain: int):
    ## TODO: this won't correctly handle if the device args
    ##   happen to include 'hackrf=' somewhere else, like in a string
    if "hackrf=" not in device_args:
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
    
    if not if_gain in [0, 8, 16, 24, 32, 40]:
        raise DeviceParameterError(
            "The HackRF One, when in receive mode, is only capable "
            "of the following if gain settings: "
            "[0, 8, 16, 24, 32, 40]. "
            f"Your specified if gain, {if_gain}, was not one of these options."
        )
    
    if not bb_gain in range(0, 62+2, 2):
        raise DeviceParameterError(
            "The HackRF One, when in receive mode, is only capable "
            "of the following bb gain settings: "
            "[0, 2, 4, 6, ..., 56, 58, 60, 62]. "
            f"Your specified bb gain, {bb_gain}, was not one of these options."
        )


def validate_hack_rf_transmit(device_args: str,
                              samp_rate: float,
                              center_freq: float,
                              if_gain: int):
    ## TODO: this won't correctly handle if the device args
    ##   happen to include 'hackrf=' somewhere else, like in a string
    if "hackrf=" not in device_args:
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
            "of the following if gain settings: "
            "[0, 1, 2, ... 45, 46, 47]. "
            f"Your specified if gain, {if_gain}, was not one of these options."
        )
