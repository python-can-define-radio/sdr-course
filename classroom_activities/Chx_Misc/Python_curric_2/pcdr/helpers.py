from typing import List, TypeVar, Union
from typeguard import typechecked

import numpy as np



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


_NON_ASCII_ERR = "Currently, this only works for characters whose `ord` value is less than 256. For now, use `bytes_to_bin_list` if you wish to use non-ASCII characters. However, this may cause unexpected results for certain characters such as '«' that have multiple possible encodings."


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
        raise ValueError(_NON_ASCII_ERR)
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
