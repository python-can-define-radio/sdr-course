import deal
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
    deal.PreContractError: ...

    Wrong size:
    >>> q.put(np.array([10, 20], dtype=np.complex64))
    Traceback (most recent call last):
      ...
    deal.PreContractError: ...
    """
    def __init__(self, qtype, dtype, chunk_size: int):
        self.qtype = qtype
        self.dtype = dtype
        self.chunk_size = chunk_size
        super().__init__()
    
    @deal.pre(lambda _: isinstance(_.item, _.self.qtype))
    @deal.pre(lambda _: _.item.dtype == _.self.dtype)
    @deal.pre(lambda _: len(_.item) == _.self.chunk_size)
    def put(self, item):
        return super().put(item)


@deal.has()
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



@deal.pre(lambda b: all(0 <= item < 256 for item in b))
@deal.ensure(lambda _: len(_.result) == len(_.b) * 8)
@deal.post(lambda result: all(x in [0, 1] for x in result))
@deal.has()
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
    bitstrs = [f"{c:08b}" for c in b]
    joined = "".join(bitstrs)
    return list(map(int, joined))


NON_ASCII_ERR = "Currently, this only works for characters whose `ord` value is less than 256. For now, use `bytes_to_bin_list` if you wish to use non-ASCII characters. However, this may cause unexpected results for certain characters such as '«' that have multiple possible encodings."
@deal.pre(lambda _: all(ord(c) < 256 for c in _.message), message=NON_ASCII_ERR)
@deal.ensure(lambda _: _.result == bytes_to_bin_list(_.message.encode("ASCII")) if all(ord(c) < 128 for c in _.message) else True)
@deal.has()
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
    return bytes_to_bin_list([ord(c) for c in message])


def hex_to_bin_list(message: np.ndarray) -> List[int]:
    """
    Converts a numpy array of hexadecimal data to a list of bits.

    Examples:

    >>> hex_to_bin_list(np.array([0x43],dtype='uint8'))
    [0, 1, 0, 0, 0, 0, 1, 1]
    
    >>> str_to_bin_list(np.array([0x43,0x42],dtype='uint8'))
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    
    >>> str_to_bin_list(np.array([0x4342],dtype='uint16'))
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
