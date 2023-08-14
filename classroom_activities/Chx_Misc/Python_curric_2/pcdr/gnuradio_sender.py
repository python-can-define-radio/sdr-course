from __future__ import annotations
from typing import List, Optional, Sequence, TypeVar
import deal
import pydash
import numpy as np
from queue import SimpleQueue, Empty
from pcdr.osmocom_queued_tx_flowgraph import queue_to__osmocom_sink, queue_to__print_blk, queue_to__string_file_sink
from pcdr.gnuradio_misc import configure_graceful_exit
from pcdr.types_and_contracts import TRealNum, TRealOrComplexNum
from pcdr.helpers import queue_to_list



T = TypeVar('T')


@deal.example(lambda: (
           np.array(queue_to_list(pad_chunk_queue([1, 2, 3], 5)))
        == np.array([[1, 2, 3, 0, 0]], dtype=np.complex64)
        ).all()
)
@deal.example(lambda: (
            np.array(queue_to_list(pad_chunk_queue([1, 2, 3], 2))) 
         == np.array([[1, 2], [3, 0]], dtype=np.complex64)
        ).all()  
)
@deal.ensure(lambda _:  \
        queue_to_list(_.result) == [] if len(_.data) == 0 else True,
        message="If data is empty, then the result is an empty queue"
)
@deal.pre(lambda _: _.chunk_size > 0)
@deal.has()
def pad_chunk_queue(data: Sequence[TRealOrComplexNum], chunk_size: int) -> SimpleQueue[np.ndarray]:
    """
    - numpy-ify
    - Pad `data` to a multiple of `chunk_size`
    - Split into chunks of that size
    - Convert to a queue of numpy arrays for gnuradio use"""

    npdata = np.array(data, dtype=np.complex64)

    ## Pad to next full chunk size, then chunk
    padlen = chunk_size - (len(npdata) % chunk_size)
    if padlen != chunk_size:
        npdata = np.concatenate([npdata, np.zeros(padlen)])
    chunked = np.split(npdata, len(npdata)/chunk_size)

    q = SimpleQueue()
    for item in chunked:
        q.put(item)
    return q


@deal.pre(lambda _: _.output_to.startswith("fn=") or _.output_to in ["hackrf", "print"])
def gnuradio_send(data: Sequence[TRealOrComplexNum],
                  center_freq: float,
                  samp_rate: float,
                  if_gain: int = 16,
                  output_to: str = "hackrf",
                  print_delay: float = 0.5,
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
