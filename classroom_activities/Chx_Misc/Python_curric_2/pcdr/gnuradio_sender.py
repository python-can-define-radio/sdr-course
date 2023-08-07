from typing import List, Optional
from numbers import Number
import deal
import pydash
import numpy as np
from queue import SimpleQueue, Empty
from pcdr.osmocom_queued_tx_flowgraph import queue_to__osmocom_sink
from pcdr.osmocom_queued_tx_flowgraph import queue_to__print_blk
from pcdr.osmocom_queued_tx_flowgraph import queue_to__string_file_sink
from pcdr.osmocom_queued_tx_flowgraph import top_block_manager


 
def __repeat_each_item(original: List[int], numtimes: int) -> List[int]:
    """Example:
    ```
    original = [1, 0]  
    numtimes = 3  
    result = [1, 1, 1, 0, 0, 0]
    ```
    """
    def repeat(item):
        return [item] * numtimes
    return pydash.flat_map(original, repeat)

assert __repeat_each_item([1, 3], 2) == [1, 1, 3, 3]


def __is_binary(x: int) -> bool:
    return x in [1, 0]


def __queue_to_list(q: SimpleQueue) -> list:
    retval = []
    while True:
        try:
            retval.append(q.get_nowait())
        except Empty:
            return retval


def pad_chunk_queue(data: List[int], chunk_size: int) -> SimpleQueue:
    """
    - Pad `data` to a multiple of `chunk_size`
    - Split into chunks of that size
    - Convert to a queue of numpy arrays for gnuradio use"""

    ## Pad to next full chunk size, then chunk
    while len(data)%chunk_size != 0:
        data.append(0)
    chunked = pydash.chunk(data, size=chunk_size)

    def makenumpy(thelist):
        return np.array(thelist, dtype=np.complex64)
    q = SimpleQueue()
    for item in map(makenumpy, chunked):
        q.put(item)
    return q


assert __queue_to_list(pad_chunk_queue([1, 2, 3], 5)) == [np.array([1, 2, 3, 0, 0], dtype=np.complex64)]
assert __queue_to_list(pad_chunk_queue([1, 2, 3], 2)) == [np.array([1, 2], dtype=np.complex64), np.array([3, 0], dtype=np.complex64)]


@deal.pre(lambda data: all(map(__is_binary, data)))
def ook_modulate(data: List[int], bit_length: int) -> List[int]:
    return __repeat_each_item(data, bit_length)
    

def frequency_shift(TODO):
    TODO
    

def gnuradio_send(data: List[int], center_freq: float, samp_rate: float, if_gain: int = 24, output_to: Optional[str] = None, print_delay=0.5, chunk_size: int = 1024):
    """`output_to` can be one of these:
        - None (default): send to osmocom sink.
        - "PRINT": print to stdout (usually the terminal).
        - any other string: interpret `output_to` as a filename. Write output data to that file.

        `print_delay` is only used if printing to stdout.
        """
    
    q = pad_chunk_queue(data, chunk_size)
    
    ## Set up and run flowgraph with the data queue we've prepared above
    if output_to == None:
        tb = queue_to__osmocom_sink(center_freq, samp_rate, chunk_size, if_gain, q)
    elif output_to == "PRINT":
        tb = queue_to__print_blk(print_delay, q, chunk_size)
    else:
        tb = queue_to__string_file_sink(output_to, q, chunk_size)
    
    tbm = top_block_manager(tb)

    ## TODO: This is NOT ideal -- would be better to detect done-ness from
    ##  inside the flowgraph if possible, so that I can use .wait() for its
    ## intended purpose.
    waittime = 1.1 * len(data)/samp_rate
    tbm.start_and_keep_open(waittime)
    
    ##   ## TODO: Do we need this? Or is it taking care of itself?
    ##   tb.stop()
    ##   tb.wait() 


