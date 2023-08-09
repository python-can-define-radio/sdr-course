from typing import List, Optional
import deal
import pydash
import numpy as np
from queue import SimpleQueue, Empty
from pcdr.osmocom_queued_tx_flowgraph import queue_to__osmocom_sink, queue_to__print_blk, queue_to__string_file_sink
from pcdr.gnuradio_misc import configure_graceful_exit




def __queue_to_list(q: SimpleQueue) -> list:
    retval = []
    while True:
        try:
            retval.append(q.get_nowait())
        except Empty:
            return retval


@deal.example(lambda: __queue_to_list(pad_chunk_queue([1, 2, 3], 5)) == [np.array([1, 2, 3, 0, 0], dtype=np.complex64)])
@deal.example(lambda: __queue_to_list(pad_chunk_queue([1, 2, 3], 2)) == [np.array([1, 2], dtype=np.complex64), np.array([3, 0], dtype=np.complex64)]) 
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


@deal.pre(lambda _: _.output_to.startswith("fn=") or _.output_to in ["hackrf", "print"])
def gnuradio_send(data: List[int],
                  center_freq: float,
                  samp_rate: float,
                  if_gain: int = 16,
                  output_to: str = "hackrf",
                  print_delay=0.5,
                  chunk_size: int = 1024,
                  device_args: str = "hackrf=0"):
    """`output_to` can be one of these:
        - "hackrf" (default): send to osmocom sink.
        - "print": print to stdout (usually the terminal).
        - "fn=abc.txt": write output data to a file named 'abc.txt'.

        `print_delay` is only used if printing to stdout.
        """
    
    q = pad_chunk_queue(data, chunk_size)
    
    ## Set up and run flowgraph with the data queue we've prepared above
    print(f"Using {output_to}.")
    if output_to == "hackrf":
        tb = queue_to__osmocom_sink(center_freq, samp_rate, chunk_size, if_gain, q, device_args)
    elif output_to == "print":
        tb = queue_to__print_blk(print_delay, q, chunk_size)
    elif output_to.startswith("fn="):
        filename = output_to[3:]  # the part after the "fn="
        tb = queue_to__string_file_sink(filename, q, chunk_size)
    else:
        raise ValueError("Shouldn't be possible if deal contracts worked.")
    
    configure_graceful_exit(tb)    
    tb.start()
    tb.wait()
